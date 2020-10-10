from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.pool import NullPool, StaticPool

from ..config import database_store_path, is_dev

# Configuration of SQLAlchemy.

if is_dev:
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
else:
    DATABASE_PATH = "sqlite://{}".format(database_store_path)
    engine = create_engine(
        DATABASE_PATH,
        poolclass=NullPool,
        connect_args={"check_same_thread": False},
        echo=True,
    )

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
