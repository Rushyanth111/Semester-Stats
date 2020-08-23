from semesterstat.common.reports import DepartmentReport
from test.BaseForDB import CommonTestClass

from sqlalchemy.orm import Session

from semesterstat.crud import (
    get_dept_by_code,
    get_dept_students,
    get_dept_subjects,
    get_dept_by_name,
    is_dept_exist,
    put_department,
    update_department,
)
from semesterstat.common import Report

from semesterstat.database import Student, Subject, Score


class DepartmentTest(CommonTestClass):
    @classmethod
    def setUpClass(cls) -> None:
        super(DepartmentTest, cls).setUpClass()
        db: Session = cls.session_create()
        cls.reports = [
            Report(
                Usn=usn,
                Name=name,
                Subcode=subcode,
                Subname=subname,
                Internals=internals,
                Externals=externals,
            )
            for (usn, name, subcode, subname, internals, externals) in [
                ("1CR10CS101", "X", "10CS65", "X", 12, 42),
                ("1CR10CS101", "X", "10CS64", "X", 16, 15),
                ("1CR10CS102", "X", "10CS54", "X", 19, 29),
                ("1CR15TE102", "X", "15MAT11", "X", 19, 55),
                ("1CR15TE102", "X", "15CSL76", "X", 38, 26),
                ("1CR15CS102", "X", "15CS55", "X", 28, 20),
            ]
        ]

        cls.student = [x.dict() for x in set([x.export_student() for x in cls.reports])]
        db.bulk_insert_mappings(Student, cls.student)

        cls.subjects = [x.export_subject().dict() for x in cls.reports]
        db.bulk_insert_mappings(Subject, cls.subjects)

        cls.scores = [x.export_score().dict() for x in cls.reports]
        db.bulk_insert_mappings(Score, cls.scores)

        db.commit()

    @classmethod
    def tearDownClass(cls) -> None:
        super(DepartmentTest, cls).setUpClass()

    def setUp(self) -> None:
        self.db = self.session_create()

    def tearDown(self) -> None:
        self.db.close()

    def test_dept_by_code(self):
        res = get_dept_by_code(self.db, "CS")
        self.assertEqual(res.Name, "X", "Department Name is Not Equal")

    def test_dept_by_name(self):
        res = get_dept_by_name(self.db, "X")
        self.assertEquals(res.Name, "X")

    def test_dept_students(self):
        res = [x.Usn for x in get_dept_students(self.db, "CS")]
        self.assertCountEqual(res, ["1CR10CS101", "1CR10CS102", "1CR15CS102"])

    def test_dept_subjects(self):
        res = [x.Code for x in get_dept_subjects(self.db, "CS")]
        self.assertCountEqual(res, ["10CS65", "10CS64", "10CS54", "15CSL76", "15CS55"])

        res = [x.Code for x in get_dept_subjects(self.db, "CS", 2015)]
        self.assertCountEqual(res, ["15CSL76", "15CS55"])

    def test_dept_exists(self):
        res = is_dept_exist(self.db, "CS")
        self.assertTrue(res)

        res = is_dept_exist(self.db, "XA")
        self.assertFalse(res)

    def test_dept_put(self):
        put_department(self.db, DepartmentReport(Code="1A", Name="OSOSOS"))
        res = is_dept_exist(self.db, "1A")
        self.assertTrue(res)

        self.db.rollback()

    def test_dept_update(self):
        update_department(
            self.db,
            DepartmentReport(Code="CS", Name="X"),
            DepartmentReport(Code="XC", Name="OSD"),
        )
        res = is_dept_exist(self.db, "XC")
        self.assertTrue(res)

        self.db.rollback()
