import random
import string
import unittest

from faker import Faker
from faker.providers import BaseProvider

import semesterstats.models as model


class SemesterStatsProvider(BaseProvider):
    def __init__(self, generator):
        super().__init__(generator)
        self.letters = string.ascii_uppercase + "1234567890"

    def gen_usn(self):
        return self.bothify("#??##??###", letters=self.letters)

    def gen_subject_code(self):
        if random.randint(0, 100) % 5 == 0:
            return self.bothify("##??L##", letters=self.letters)
        else:
            return self.bothify("##??##", letters=self.letters)

    def gen_batch(self):
        pass

    def gen_scheme(self):
        pass


class TestModelInterface(unittest.TestCase):
    def setUp(self):
        self.db = model.ModelInterface()
        Faker.seed(0)
        self.fake = Faker()
        self.fake.add_provider(SemesterStatsProvider)

    def test_insert_department(self):
        d = model.DepartmentModel(DepartmentCode="XTX", DepartmentName="Tester")
        self.db.insert_department(d)

    def test_insert_department_bulk(self):

        d = [
            model.DepartmentModel(
                DepartmentCode=self.fake.gen_usn(), DepartmentName=self.fake.name()
            )
            for _ in range(300)
        ]

        self.db.insert_department_bulk(d)

    def test_insert_student(self):
        d = model.DepartmentModel(DepartmentCode="XTX", DepartmentName="Tester")
        self.db.insert_department(d)

        d = model.StudentModel(
            StudentUSN=self.fake.gen_usn(),
            StudentName=self.fake.name(),
            StudentBatch=2016,
            StudentDepartment="XTX",
        )

        self.assertEqual(self.db.insert_student(d), 1)

    def test_insert_student_bulk(self):
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
