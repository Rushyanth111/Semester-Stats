from typing import Callable
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from semesterstat.database.models import (
    Base,
    BatchSchemeInfo,
    Department,
)


class CommonTestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # Set Up Test Data
        cls.engine = create_engine(
            "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
        )
        cls.session_create: Callable[[], Session] = sessionmaker(
            bind=cls.engine, autocommit=False, autoflush=False
        )

        Base.metadata.create_all(bind=cls.engine)

        # Creating Some Data.
        db: Session = cls.session_create()

        # Only Keep Common Stuff Here.
        cls.depts = [
            {"Code": code, "Name": name}
            for (code, name) in [
                ("CS", "X"),
                ("IS", "X"),
                ("TE", "X"),
                ("ME", "X"),
                ("AE", "X"),
            ]
        ]

        db.bulk_insert_mappings(Department, cls.depts)

        cls.batch_scheme = [
            {"Batch": batch, "Scheme": scheme}
            for (batch, scheme) in [
                (2010, 2010),
                (2011, 2010),
                (2012, 2010),
                (2013, 2010),
                (2014, 2010),
                (2015, 2015),
                (2016, 2015),
                (2017, 2017),
            ]
        ]

        db.bulk_insert_mappings(BatchSchemeInfo, cls.batch_scheme)

        db.commit()

    @classmethod
    def tearDownClass(cls) -> None:
        # Dispose Engine
        cls.engine.dispose()
