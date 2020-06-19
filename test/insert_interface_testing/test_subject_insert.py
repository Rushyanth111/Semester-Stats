from test.BaseClassUtils import BaseClassUnitTestCase
import semesterstats.models as model
import random


class SubjectInsertTest(BaseClassUnitTestCase):
    def setUp(self):
        self.db = model.ModelInterface()
        self.bnc_init()

    def test_insert_subject(self):
        d = model.DepartmentModel(DepartmentCode="XTX", DepartmentName="Tester")
        self.db.insert_department(d)
        d = model.SubjectModel(
            SubjectCode=self.fake.gen_subject_code(),
            SubjectName=self.fake.name(),
            SubjectSemester=random.randint(1, 8),
            SubjectScheme=random.randint(2015, 2018),
            SubjectDepartment="XTX",
        )

        self.assertEqual(self.db.insert_subject(d), 1)

    def test_insert_subject_bulk(self):
        d = model.DepartmentModel(DepartmentCode="XTX", DepartmentName="Tester")
        self.db.insert_department(d)
        d = [
            model.SubjectModel(
                SubjectCode=self.fake.gen_subject_code(),
                SubjectName=self.fake.name(),
                SubjectSemester=random.randint(1, 8),
                SubjectScheme=random.randint(2015, 2018),
                SubjectDepartment="XTX",
            )
            for x in range(300)
        ]

        self.db.insert_subject_bulk(d)
