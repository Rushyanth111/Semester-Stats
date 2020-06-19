import semesterstats.models as model
from test.BaseClassUtils import BaseClassUnitTestCase


class StudentInsert(BaseClassUnitTestCase):
    def setUp(self):
        self.db = model.ModelInterface()
        self.bnc_init()

    def test_single_insert(self):
        d = model.DepartmentModel(DepartmentCode="XTX", DepartmentName="Tester")
        self.db.insert_department(d)

        d = model.StudentModel(
            StudentUSN=self.fake.gen_usn(),
            StudentName=self.fake.name(),
            StudentBatch=2016,
            StudentDepartment="XTX",
        )

        self.assertEqual(self.db.insert_student(d), 1)

    def test_insert_bulk(self):
        d = model.DepartmentModel(DepartmentCode="XTX", DepartmentName="Tester")
        self.db.insert_department(d)
        usns = [self.fake.gen_usn() for x in range(300)]

        d = [
            model.StudentModel(
                StudentUSN=usns[x],
                StudentName=self.fake.name(),
                StudentBatch=2016,
                StudentDepartment="XTX",
            )
            for x in range(300)
        ]

        self.db.insert_student_bulk(d)

    def test_insert_duplicate(self):
        pass

    def test_insert_conflict(self):
        pass
