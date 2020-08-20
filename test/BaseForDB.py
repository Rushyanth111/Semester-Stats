import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.pool import StaticPool

from semesterstat.database.models import Base


class CommonTestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Set Up Test Data
        cls.engine = create_engine(
            "sqlite://",
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
            echo=False,
        )
        cls.session_create = sessionmaker(
            bind=cls.engine, autocommit=False, autoflush=False
        )

        Base.metadata.create_all(bind=cls.engine)

    @classmethod
    def tearDownClass(cls) -> None:
        # Dispose Engine
        cls.engine.dispose()
