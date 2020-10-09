import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from semesterstat.database.models import Base
from tests.dbdata import __input_data


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


@pytest.fixture(scope="session")
def rootdir():
    return os.path.abspath(os.getcwd())
