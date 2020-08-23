from test.BaseForDB import CommonTestClass

from sqlalchemy.orm.session import Session

from semesterstat.common import Report
from semesterstat.common.reports import StudentReport
from semesterstat.crud.batch import BatchQuery
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
        super(BatchFunctionsTest, cls).tearDownClass()

    def setUp(self):
        self.db: Session = self.session_create()

    def tearDown(self) -> None:
        self.db.close()

    def test_default(self) -> None:

        res = BatchQuery(self.db, 2010).export_usns()

        self.assertCountEqual(
            ["1CR10CS101", "1CR10CS102"], res, "Usn's Are not Matched."
        )

    def test_semester(self) -> None:

        res = BatchQuery(self.db, 2010).sem(6).export_usns()
        self.assertCountEqual(["1CR10CS101"], res, "Too many/Too Few in Semester")

        res = BatchQuery(self.db, 2010).sem(7).export_usns()
        self.assertFalse(res)

    def test_department(self) -> None:

        res = BatchQuery(self.db, 2010).dept("CS").export_usns()
        self.assertCountEqual(
            ["1CR10CS101", "1CR10CS102"], res, "Usn's Are not Matched."
        )

        res = BatchQuery(self.db, 2010).dept("TE").export_usns()
        self.assertFalse(res, "Usn's Are not Matched.")

    def test_backlog(self) -> None:

        res = BatchQuery(self.db, 2010).backlog().export_usns()

        self.assertCountEqual(["1CR10CS101"], res, "Backlog Numbers Are Wrong")

    def test_detain(self) -> None:

        res = BatchQuery(self.db, 2010).detain(1).export_usns()

        self.assertCountEqual(["1CR10CS101"], res, "Usn's Are not Matched.")

    def test_report(self) -> None:

        res = BatchQuery(self.db, 2010).export_report()

        for r in res:
            self.assertIsInstance(r, StudentReport)

    def test_sem_dept(self):

        res = BatchQuery(self.db, 2015).dept("TE").sem(1).export_usns()
        print(res)
        self.assertCountEqual(res, ["1CR15TE102"])
