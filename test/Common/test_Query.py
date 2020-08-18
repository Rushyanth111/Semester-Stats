import unittest
from semesterstat.common.query import get_scheme, get_student_usn_list, get_subject_list
from semesterstat.database import (
    session_create,
    BatchSchemeInfo,
    Department,
    Student,
    Subject,
)
from sqlalchemy import create_engine


class CommonQueryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:

        # Create a New Engine:
        engine = create_engine("sqlite://")
        session_create.configure(bind=engine)
        Department.metadata.create_all(engine)
        db = session_create()
        db.query(Department).delete()
        db.commit()

        x = BatchSchemeInfo(Batch=2017, Scheme=2017)
        db.add(x)

        x = Department(Code="CS", Name="ComputerScienceDept")
        db.add(x)

        x = Student(Usn="1CR17CS117", Name="Rushyanth S", Batch=2017, Department="CS")
        db.add(x)

        x = Subject(
            Code="17CS51", Name="Entr", Semester=5, Scheme=2017, Department="CS"
        )
        db.add(x)
        db.commit()
        db.close()

    def setUp(self) -> None:
        self.db = session_create()

    def tearDown(self) -> None:
        self.db.close()

    def test_get_scheme(self) -> None:
        self.assertEqual(get_scheme(self.db, 2017), 2017)

    def test_get_student_usn_list(self) -> None:
        self.assertListEqual(get_student_usn_list(self.db, 2017, "CS"), ["1CR17CS117"])

    def test_get_subject_list(self) -> None:
        self.assertListEqual(get_subject_list(self.db, 5, 2017), ["17CS51"])
