from typing import Callable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from ..Config import database_store_path

# Configuration of SQLAlchemy.
database_store_path = "sqlite:///{}".format(database_store_path)

engine = create_engine(database_store_path, connect_args={"check_same_thread": False})

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
