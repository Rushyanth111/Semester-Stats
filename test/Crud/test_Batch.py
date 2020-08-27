from semesterstat.common.reports import StudentReport
from semesterstat.crud.batch import get_batch_students_usn
from test.BaseForDB import CommonTestClass

from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound

from semesterstat.common import Report
from semesterstat.crud import (
    get_batch_scores,
    get_batch_students,
    is_batch_exists,
    get_scheme,
)
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
                ("1CR15CS101", "X", "15CS65", "X", 12, 42),
                ("1CR15CS101", "X", "15CS64", "X", 16, 15),
                ("1CR15CS102", "X", "15CS54", "X", 19, 29),
                ("1CR17TE102", "X", "17MAT11", "X", 19, 55),
                ("1CR17TE102", "X", "17CSL76", "X", 38, 26),
                ("1CR17CS102", "X", "17CS55", "X", 28, 20),
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
        self.db = self.session_create()

    def tearDown(self) -> None:
        self.db.close()

    def test_get_scheme(self):
        res = get_scheme(self.db, 2015)
        self.assertEqual(res, 2015)

        res = get_scheme(self.db, 2016)
        self.assertEqual(res, 2015)

        self.assertRaises(NoResultFound, get_scheme(self.db, 2014))

    def test_is_batch_exists(self):
        self.assertTrue(is_batch_exists(self.db, 2017))
        self.assertFalse(is_batch_exists(self.db, 2014))

    def test_get_batch_students(self):
        res = get_batch_students(self.db, 2015)
        self.assertIsInstance(res[0], StudentReport)
        self.assertCountEqual(["1CR15CS101", "1CR15CS102"], [x.Usn for x in res])

        res = get_batch_students(self.db, 2015, "CS")
        self.assertIsInstance(res[0], StudentReport)
        self.assertCountEqual(["1CR15CS101", "1CR15CS102"], [x.Usn for x in res])

        res = get_batch_students(self.db, 2015, "TE")
        self.assertFalse(res)

    def test_get_batch_students_usn(self):
        res = get_batch_students_usn(self.db, 2015)
        self.assertIsInstance(res, list)
        self.assertCountEqual(["1CR15CS101", "1CR15CS102"], res)

        res = get_batch_students_usn(self.db, 2015, "CS")
        self.assertIsInstance(res, list)
        self.assertCountEqual(["1CR15CS101", "1CR15CS102"], res)

        res = get_batch_students_usn(self.db, 2015, "TE")
        self.assertFalse(res)

    def test_get_batch_scores(self):
        res = get_batch_scores(self.db, 2015)

        res_a = ["1CR15CS101", "1CR15CS102"]
        res_a_scores = ["15CS65", "15CS64", "15CS54"]
        self.assertEqual(len(res), 2)
        self.assertCountEqual(res_a, [x.Usn for x in res])
        self.assertCountEqual(
            res_a_scores, [y.SubjectCode for x in res for y in x.Scores]
        )

        res = get_batch_scores(self.db, 2014)
        self.assertFalse(res)

        res = get_batch_scores(self.db, 2015, sem=6)
        self.assertCountEqual(res_a[0:1], [x.Usn for x in res])
        self.assertCountEqual(
            res_a_scores[0:2], [y.SubjectCode for x in res for y in x.Scores]
        )

        res = get_batch_scores(self.db, 2015, dept="CS", sem=6)
        self.assertCountEqual(res_a[0:1], [x.Usn for x in res])
        self.assertCountEqual(
            res_a_scores[0:2], [y.SubjectCode for x in res for y in x.Scores]
        )

        res = get_batch_scores(self.db, 2015, dept="CS", sem=7)
        self.assertFalse(res)
