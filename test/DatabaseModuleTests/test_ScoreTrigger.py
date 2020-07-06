from semesterstat.Database import Score, BacklogHistory, Student, Subject
from peewee import EXCLUDED
import unittest


class ScoreTriggerTest(unittest.TestCase):
    def setUp(self):

        Student.insert(
            Usn="1CR17CS001", Name="Dummy", Batch=2016, Department="CS",
        ).execute()

        Subject.insert(
            Code="17CS56", Name="Dummy", Semester=5, Scheme=2017, Department="CS",
        ).execute()

    def tearDown(self):
        Score.delete().execute()
        BacklogHistory.delete().execute()
        Student.delete().execute()
        Subject.delete().execute()

    def test_check_trigger_working(self):

        Score.insert(
            Usn="1CR17CS001", SubjectCode="17CS56", Internals=56, Externals=22,
        ).execute()

        Score.insert(
            Usn="1CR17CS001", SubjectCode="17CS56", Internals=56, Externals=26,
        ).on_conflict(
            conflict_target=[Score.Usn, Score.SubjectCode],
            update={
                Score.Internals: EXCLUDED.Internals,
                Score.Externals: EXCLUDED.Externals,
            },
            where=(
                (Score.Externals + Score.Internals)
                < (EXCLUDED.Internals + EXCLUDED.Externals)
            ),
        ).execute()

        count = BacklogHistory.select().count()

        assert count == 1

    def test_check_trigger_ignores_lower_score(self):
        Score.insert(
            Usn="1CR17CS001", SubjectCode="17CS56", Internals=56, Externals=22,
        ).execute()

        Score.insert(
            Usn="1CR17CS001", SubjectCode="17CS56", Internals=56, Externals=20,
        ).on_conflict(
            conflict_target=[Score.Usn, Score.SubjectCode],
            update={
                Score.Internals: EXCLUDED.Internals,
                Score.Externals: EXCLUDED.Externals,
            },
            where=(
                (Score.Externals + Score.Internals)
                < (EXCLUDED.Internals + EXCLUDED.Externals)
            ),
        ).execute()

        count = BacklogHistory.select().count()

        assert count == 0
