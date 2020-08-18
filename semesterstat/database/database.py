from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..Config import database_store_path

# Configuration of SQLAlchemy.
database_store_path = "sqlite:///{}".format(database_store_path)

engine = create_engine(database_store_path, connect_args={"check_same_thread": False})

# Exporting the Session_create Object
session_create = sessionmaker(bind=engine, autocommit=False, autoflush=False)
