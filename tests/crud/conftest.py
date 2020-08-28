import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool
from typing import Callable
from semesterstat.database.models import Base
from semesterstat.database import Department, BatchSchemeInfo, Student, Subject, Score
from semesterstat.common import Report


@pytest.fixture(scope="package")
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
            ("CS", "X"),
            ("IS", "X"),
            ("TE", "X"),
            ("ME", "X"),
            ("AE", "X"),
        ]
    ]

    _db.bulk_insert_mappings(Department, depts)

    batch_scheme = [
        {"Batch": batch, "Scheme": scheme}
        for (batch, scheme) in [(2015, 2015), (2016, 2015), (2017, 2017)]
    ]

    _db.bulk_insert_mappings(BatchSchemeInfo, batch_scheme)

    reports = [
        Report(
            Usn=usn,
            Name=name,
            Subcode=subcode,
            Subname=subname,
            Internals=internals,
            Externals=externals,
        )
        for (usn, name, subcode, subname, internals, externals) in [
            ("1CR15CS101", "X", "15CS65", "X", 12, 42),
            ("1CR15CS101", "X", "15CS64", "X", 16, 15),
            ("1CR15CS102", "X", "15CS54", "X", 19, 29),
            ("1CR17TE102", "X", "17MAT11", "X", 19, 55),
            ("1CR17TE102", "X", "17CSL76", "X", 38, 26),
            ("1CR17CS102", "X", "17CS55", "X", 28, 20),
        ]
    ]
    student = [x.dict() for x in set([x.export_student() for x in reports])]
    _db.bulk_insert_mappings(Student, student)

    subjects = [x.export_subject().dict() for x in reports]
    _db.bulk_insert_mappings(Subject, subjects)

    scores = [x.export_score().dict() for x in reports]
    _db.bulk_insert_mappings(Score, scores)

    _db.commit()
    _db.close()

    # Return the Session Data.
    yield session_create

    engine.dispose()


@pytest.fixture(scope="function")
def db(def_db):
    _db: Session = def_db()
    yield _db

    _db.close()
