import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from semesterstat.database.models import Base
from semesterstat.database import Department, BatchSchemeInfo


def __input_data(db: Session):
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

    db.bulk_insert_mappings(Department, depts)

    batch_scheme = [
        {"Batch": batch, "Scheme": scheme}
        for (batch, scheme) in [(2015, 2015), (2016, 2015), (2017, 2017)]
    ]
    db.bulk_insert_mappings(BatchSchemeInfo, batch_scheme)


@pytest.fixture(scope="package")
def engine():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )

    Base.metadata.create_all(bind=engine)

    db = Session(bind=engine)
    __input_data(db)
    db.commit()
    db.close()

    # Return the Session Data.
    yield engine

    engine.dispose()


@pytest.fixture(scope="function")
def db(engine):
    _engine = engine

    # Make a new Connection.
    conn = _engine.connect()

    # OverArching Transaction, doesn't matter what happened before.
    trans = conn.begin()

    session = Session(bind=conn)

    yield session

    # Dispose the objects in memory, we don't need them.
    session.close()

    # Rollback all Commits.
    trans.rollback()

    # Close the connection
    conn.close()
