import unittest
import semesterstats.models as model
from faker import Faker
import random


class TestModelInterface(unittest.TestCase):
    def setUp(self):
        self.db = model.ModelInterface()
        Faker.seed(0)
        self.fake = Faker()

    def test_insert_department(self):
        d = model.DepartmentModel(DepartmentCode="XTX", DepartmentName="Tester")
        self.db.insert_department(d)

    def test_insert_student(self):
        d = model.DepartmentModel(DepartmentCode="XTX", DepartmentName="Tester")
        self.db.insert_department(d)

        d = model.StudentModel(
            StudentUSN="1CR17CS117",
            StudentName="Rushyanth S",
            StudentBatch=2016,
            StudentDepartment="XTX",
        )

        self.assertEqual(self.db.insert_student(d), 1)

    def test_insert_subject(self):
        d = model.DepartmentModel(DepartmentCode="XTX", DepartmentName="Tester")
        self.db.insert_department(d)
        d = model.SubjectModel(
            SubjectCode=self.fake.bothify("#??##??###"),
            SubjectName=self.fake.name(),
            SubjectSemester=random.randint(1, 8),
            SubjectScheme=random.randint(2015, 2018),
            SubjectDepartment="XTX",
        )

        self.assertEqual(self.db.insert_subject(d), 1)

    def test_insert_score(self):

        fake_subject_code = self.fake.bothify("##??##")
        fake_serial_number = self.fake.bothify("#??##??###")

        d = model.DepartmentModel(DepartmentCode="XTX", DepartmentName="Tester")
        self.db.insert_department(d)
        d = model.StudentModel(
            StudentUSN=fake_serial_number,
            StudentName=self.fake.name(),
            StudentBatch=2016,
            StudentDepartment="XTX",
        )

        self.db.insert_student(d)
        d = model.SubjectModel(
            SubjectCode=fake_subject_code,
            SubjectName=self.fake.name(),
            SubjectSemester=random.randint(1, 8),
            SubjectScheme=random.randint(2015, 2018),
            SubjectDepartment="XTX",
        )

        self.db.insert_subject(d)

        d = model.ScoreModel(
            ScoreSerialNumber=fake_serial_number,
            ScoreSubjectCode=fake_subject_code,
            ScoreYear=random.randint(1, 8),
            ScoreYearIndicator=random.randint(0, 1),
            ScoreExternals=random.randint(0, 40),
            ScoreInternals=random.randint(0, 60),
        )

        self.assertEqual(self.db.insert_score(d), 1)


if __name__ == "__main__":
    unittest.main()
