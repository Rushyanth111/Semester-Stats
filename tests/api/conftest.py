import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from semesterstat.api import app
from semesterstat.database.database import get_db
from semesterstat.database.models import Base, Score, Student, Subject
from semesterstat.reports import ScoreReport, StudentReport, SubjectReport
from tests.dbdata import __input_data

engine = create_engine(
    "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
)
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def db_override():
    conn = engine.connect()
    trans = conn.begin()
    try:
        session = Session(bind=conn)
        yield session
    finally:
        session.close()
        trans.rollback()
        conn.close()


app.dependency_overrides[get_db] = db_override


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as cl:
        yield cl


@pytest.fixture(scope="package", autouse=True)
def _data():
    db = Session(bind=engine)

    # Inserting Common Data Between the Tests:
    __input_data(db)

    student_data = [
        StudentReport(Name=name, Usn=code).dict()
        for (code, name) in [
            ("1CR15CS101", "Mattie Schultz"),
            ("1CR15CS102", "Johnny Pope"),
            ("1CR17TE102", "Ray Guzman"),
            ("1CR17CS102", "Aaron Vargas"),
        ]
    ]

    db.bulk_insert_mappings(Student, student_data)

    subject_data = [
        SubjectReport(
            Code=code,
            Name=name,
            MinExt=minext,
            MinTotal=mintotal,
            MaxTotal=100,
            Credits=credits,
        ).dict()
        for (code, name, minext, mintotal, credits) in [
            ("15CS65", "X", 21, 40, 4),
            ("15CS64", "X", 21, 40, 4),
            ("15CS54", "X", 21, 40, 4),
            ("17MAT11", "X", 21, 40, 4),
            ("17CSL76", "X", 21, 40, 2),
            ("17CS55", "X", 21, 40, 4),
        ]
    ]
    db.bulk_insert_mappings(Subject, subject_data)

    score_data = [
        ScoreReport(
            Usn=usn, SubjectCode=subcode, Internals=internals, Externals=externals
        ).dict()
        for (usn, subcode, internals, externals) in [
            ("1CR15CS101", "15CS65", 12, 42),  # 54 - SC
            ("1CR15CS101", "15CS64", 16, 15),  # Fail
            ("1CR15CS102", "15CS54", 19, 29),  # 48 - SC
            ("1CR17TE102", "17MAT11", 19, 55),  # 74 - FCD
            ("1CR17TE102", "17CSL76", 38, 26),  # 64 - FC
            ("1CR17CS102", "17CS55", 28, 20),  # Fail
        ]
    ]
    db.bulk_insert_mappings(Score, score_data)
    db.commit()
    db.close()
