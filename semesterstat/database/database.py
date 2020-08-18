from sqlalchemy.pool.impl import NullPool
from typing import Callable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.pool import StaticPool
from ..Config import database_store_path

# Configuration of SQLAlchemy.

DATABASE_PATH = "sqlite://{}".format(database_store_path)

if database_store_path == "":
    engine = create_engine(
        DATABASE_PATH, connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
else:
    engine = create_engine(DATABASE_PATH, poolclass=NullPool)

# Exporting the Session_create Object
session_create: Callable[[], Session] = sessionmaker(
    bind=engine, autocommit=False, autoflush=False
)


# Helper Function that cleans up after itself.
def get_db() -> Session:
    db = session_create()
    try:
        yield db
    finally:
        db.close()
