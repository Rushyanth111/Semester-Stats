from test.BaseForDB import CommonTestClass

from semesterstat.common import SubjectReport
from semesterstat.crud import (
    get_subject,
    put_subject,
    update_subject,
    is_subject_exist,
    is_subjects_exists,
)
from semesterstat.database import Subject


class SubjectTests(CommonTestClass):
    @classmethod
    def setUpClass(cls) -> None:
        super(SubjectTests, cls).setUpClass()

        db = cls.session_create()

        cls.reports = [
            SubjectReport(Code=x, Name=y).dict()
            for (x, y) in [
                ("10CS65", "EM65"),
                ("10CS14", "EM14"),
                ("10CS25", "EM25"),
                ("10CS566", "EM66"),
                ("10CSL56", "EM56"),
            ]
        ]
        db.bulk_insert_mappings(Subject, cls.reports)

        db.commit()

    @classmethod
    def tearDownClass(cls) -> None:
        super(SubjectTests, cls).tearDownClass()

    def setUp(self) -> None:
        self.db = self.session_create()

    def tearDown(self) -> None:
        self.db.close()

    def test_get_subject(self) -> None:
        res = get_subject(self.db, "10CS65")
        self.assertEqual(res.Name, "EM65")

    def test_put_student(self) -> None:
        put_subject(self.db, SubjectReport(Code="10CS11", Name="EM11"))
        self.assertTrue(is_subject_exist(self.db, "10CS11"))

        self.db.rollback()

    def test_update_student(self) -> None:
        update_subject(
            self.db,
            SubjectReport(Code="10CS14", Name="X"),
            SubjectReport(Code="10CS11", Name="EM11"),
        )
        self.assertTrue(is_subject_exist(self.db, "10CS11"))

        self.db.rollback()

    def test_is_subject_exists(self):
        res = is_subject_exist(self.db, "10CS14")
        self.assertTrue(res)
        res = is_subject_exist(self.db, "10CS22")
        self.assertFalse(res)

    def test_is_subjects_exist(self):
        res = is_subjects_exists(self.db, ["10CS14", "10CS25"])
        self.assertTrue(res)

        res = is_subjects_exists(self.db, ["10CS14", "10CS26"])
        self.assertFalse(res)
