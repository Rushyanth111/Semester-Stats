import unittest
from semesterstat.database import Student, Score, Subject


class StudentTests(unittest.TestCase):
    def test_student_update_cascade(self):
        # Insert a Student, Insert a Score with the same USN, Update.
        Subject.insert(
            Code="17CS56", Name="Dummy", Semester=5, Scheme=2017, Department="CS",
        ).execute()

        Student.insert(
            Usn="1CR17CS001", Name="Dummy", Batch=2016, Department="CS",
        ).execute()

        Score.insert(
            Usn="1CR17CS001", SubjectCode="17CS56", Internals="56", Externals="100"
        ).execute()

        Student.update(Usn="1CR17CS002").where(Student.Usn == "1CR17CS001").execute()

        count = Score.select().where(Score.Usn == "1CR17CS002").count()

        assert count == 1
