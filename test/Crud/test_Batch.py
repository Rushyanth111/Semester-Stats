from test.BaseForDB import CommonTestClass

from sqlalchemy.orm.session import Session

from semesterstat.common import Report
from semesterstat.crud.batch import BatchCrud
from semesterstat.database import Score, Student, Subject


class BatchFunctionsTest(CommonTestClass):
    @classmethod
    def setUpClass(cls) -> None:
        super(BatchFunctionsTest, cls).setUpClass()

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
                ("1CR15TE102", "X", "10MAT11", "X", 19, 55),
                ("1CR15TE102", "X", "10CSL76", "X", 38, 26),
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
        super(BatchFunctionsTest, cls).tearDownClass()

    def setUp(self):
        self.db: Session = self.session_create()

    def tearDown(self) -> None:
        self.db.close()

    def test_default(self):
        res = BatchCrud(self.db, 2010).export_student_report()
        self.assertCountEqual(
            [x.Usn for x in res], ["1CR10CS101", "1CR10CS102"], "USN is not Correct",
        )

        res = BatchCrud(self.db, 2011).export_student_report()

        self.assertCountEqual([x.Usn for x in res], [])

    def test_default_usnonly(self):
        res = BatchCrud(self.db, 2010).export_usn_list()
        self.assertCountEqual(
            res, ["1CR10CS101", "1CR10CS102"], "USN is not Correct",
        )

    def test_department_filter(self):
        pass

    def test_semester_filter(self):
        pass

    def test_department_semester_filter(self):
        pass

    def test_detained_filter(self):
        res = BatchCrud(self.db, 2010).backlog_filter(40, 21).export_usn_list(True, 1)

        self.assertCountEqual(["1CR10CS101"], res)

        res = BatchCrud(self.db, 2010).backlog_filter(40, 21).export_usn_list(True, 2)

        self.assertFalse(res)

    def test_backlog_filter(self):
        res = BatchCrud(self.db, 2010).backlog_filter(40, 21).export_student_report()

        self.assertCountEqual([y.SubjectCode for y in res[0].Scores], ["10CS64"])
