from semesterstat.common.reports import ScoreReport, StudentReport, SubjectReport
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool
from typing import Callable
from semesterstat.database.models import Base
from semesterstat.database import Department, BatchSchemeInfo, Student, Subject, Score


@pytest.fixture(scope="module")
def def_db():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    session_create: Callable[[], Session] = sessionmaker(
        bind=engine, autocommit=False, autoflush=False
    )

    Base.metadata.create_all(bind=engine)

    _db: Session = session_create()
    depts = [
        {"Code": code, "Name": name}
        for (code, name) in [
            ("CS", "Computer Science"),
            ("IS", "Information Science"),
            ("TE", "Telecommunication"),
            ("ME", "Mechanical Engineering"),
            ("AE", "Aeronautical Engineering"),
        ]
    ]

    _db.bulk_insert_mappings(Department, depts)

    batch_scheme = [
        {"Batch": batch, "Scheme": scheme}
        for (batch, scheme) in [(2015, 2015), (2016, 2015), (2017, 2017)]
    ]

    _db.bulk_insert_mappings(BatchSchemeInfo, batch_scheme)

    stu_data = [
        StudentReport(Usn=usn, Name=name)
        for (usn, name) in [
            ("1CR15CS101", "X"),
            ("1CR15CS102", "X"),
            ("1CR17TE102", "X"),
            ("1CR17CS102", "X"),
        ]
    ]
    student = [x.dict() for x in stu_data]
    _db.bulk_insert_mappings(Student, student)

    subect_data = [
        SubjectReport(
            Code=code, Name=name, MinExt=minext, MinTotal=mintotal, Credits=credits
        )
        for (code, name, minext, mintotal, credits) in [
            ("15CS65", "X", 21, 35, 4),
            ("15CS64", "X", 21, 35, 4),
            ("15CS54", "X", 21, 35, 4),
            ("17MAT11", "X", 21, 35, 4),
            ("17CSL76", "X", 21, 35, 2),
            ("17CS55", "X", 21, 35, 4),
        ]
    ]
    subjects = [x.dict() for x in subect_data]
    _db.bulk_insert_mappings(Subject, subjects)

    score_data = [
        ScoreReport(
            Usn=usn, SubjectCode=subcode, Internals=internals, Externals=externals,
        )
        for (usn, subcode, internals, externals) in [
            ("1CR15CS101", "15CS65", 12, 42),
            ("1CR15CS101", "15CS64", 16, 15),
            ("1CR15CS102", "15CS54", 19, 29),
            ("1CR17TE102", "17MAT11", 19, 55),
            ("1CR17TE102", "17CSL76", 38, 26),
            ("1CR17CS102", "17CS55", 28, 20),
        ]
    ]
    scores = [x.dict() for x in score_data]
    _db.bulk_insert_mappings(Score, scores)

    _db.commit()
    _db.close()

    # Return the Session Data.
    yield session_create

    engine.dispose()


@pytest.fixture(scope="function")
def db(def_db):
    _db: Session = def_db()
    _db.begin_nested()
    yield _db

    _db.rollback()
