from test.BaseClassUtils import BaseClassUnitTestCase
import semesterstats.models as model
import random


class TestScoreInsert(BaseClassUnitTestCase):
    def setUp(self):
        self.db = model.ModelInterface()
        self.bnc_init()

    def test_insert_single_score(self):

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
            ScoreSemester=random.randint(1, 8),
            ScoreExternals=random.randint(0, 40),
            ScoreInternals=random.randint(0, 60),
        )

        self.assertEqual(self.db.insert_score(d), 1)

    def test_score_multiple(self):
        pass

    def test_score_conflict(self):
        pass

    def test_score_update(self):
        pass

    def test_backlog_retained(self):
        pass

    def test_backlog_added(self):
        pass
