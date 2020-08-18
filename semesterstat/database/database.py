from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Configuration of SQLAlchemy.
database_store_path = "sqlite:///:memory:"

engine = create_engine(database_store_path, connect_args={"check_same_thread": False})

local_session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
