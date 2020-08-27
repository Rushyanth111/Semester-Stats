from semesterstat.common.reports import StudentReport
from test.BaseForDB import CommonTestClass

from sqlalchemy.orm import Session

from semesterstat.common import Report
from semesterstat.database import Score, Student, Subject

from semesterstat.crud import (
    get_student,
    get_student_scores,
    get_student_scores_by_semester,
    get_student_subject,
    is_student_exists,
    put_student,
    update_student,
)


class StudentCrudTests(CommonTestClass):
    @classmethod
    def setUpClass(cls) -> None:
        super(StudentCrudTests, cls).setUpClass()
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
                ("1CR10CS101", "OSAS", "10MAT11", "X", 19, 29),
                ("1CR10CS101", "OSAS", "10MAT21", "X", 40, 40),
                ("1CR10CS101", "OSAS", "10CS61", "X", 16, 15),
                ("1CR10CS101", "OSAS", "10CS62", "X", 10, 2),
                ("1CR10CS101", "OSAS", "10CS63", "X", 12, 10),
                ("1CR10CS101", "OSAS", "10CS64", "X", 20, 30),
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
        super(StudentCrudTests, cls).setUpClass()

    def setUp(self) -> None:
        self.db = self.session_create()

    def tearDown(self) -> None:
        self.db.close()

    def test_get_student(self):
        res = get_student(self.db, "1CR10CS101")
        self.assertEquals(res.Name, "OSAS")

    def test_get_student_scores(self):
        res = get_student_scores(self.db, "1CR10CS101")
        res = [x.SubjectCode for x in res]

        self.assertCountEqual(
            ["10MAT11", "10MAT21", "10CS61", "10CS62", "10CS63", "10CS64"], res
        )

    def test_get_student_scores_by_semester(self):
        res = get_student_scores_by_semester(self.db, "1CR10CS101", 6)
        res = [x.SubjectCode for x in res]
        self.assertCountEqual(["10CS61", "10CS62", "10CS63", "10CS64"], res)

    def test_student_subject(self):
        res = get_student_subject(self.db, "1CR10CS101", "10CS62")
        self.assertEquals(res.Internals, 10)
        self.assertEqual(res.Externals, 2)

    def test_get_student_backlogs(self):
        pass

    def test_is_student(self):
        res = is_student_exists(self.db, "1CR10CS101")
        self.assertTrue(res)
        res = is_student_exists(self.db, "1CR10CS102")
        self.assertFalse(res)

    def test_put_student(self):
        put_student(self.db, StudentReport(Usn="1CR10CS102", Name="XX"))
        res = is_student_exists(self.db, "1CR10CS102")
        self.assertTrue(res)
        self.db.rollback()

    def test_update_student(self):
        update_student(
            self.db, "1CR10CS101", StudentReport(Usn="1CR10CS102", Name="XX"),
        )
        res = is_student_exists(self.db, "1CR10CS102")
        self.assertTrue(res)
        self.db.rollback()
