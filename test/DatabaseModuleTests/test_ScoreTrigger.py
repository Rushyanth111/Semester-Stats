from semesterstat.Database import Score, BacklogHistory, Student, Department, Subject
from peewee import EXCLUDED
import unittest


class ScoreTriggerTest(unittest.TestCase):
    def setUp(self):

        Student.insert(
            StudentUSN="1CR17CS001",
            StudentName="Dummy",
            StudentBatch=2016,
            StudentDepartment="CS",
        ).execute()

        Subject.insert(
            SubjectCode="17CS56",
            SubjectName="Dummy",
            SubjectSemester=5,
            SubjectScheme=2017,
            SubjectDepartment="CS",
        ).execute()

    def tearDown(self):
        Score.delete().execute()
        BacklogHistory.delete().execute()
        Student.delete().execute()
        Subject.delete().execute()

    def test_check_trigger_working(self):

        Score.insert(
            ScoreSerialNumber="1CR17CS001",
            ScoreSubjectCode="17CS56",
            ScoreInternals=56,
            ScoreExternals=22,
        ).execute()

        Score.insert(
            ScoreSerialNumber="1CR17CS001",
            ScoreSubjectCode="17CS56",
            ScoreInternals=56,
            ScoreExternals=26,
        ).on_conflict(
            conflict_target=[Score.ScoreSerialNumber, Score.ScoreSubjectCode],
            update={
                Score.ScoreInternals: EXCLUDED.ScoreInternals,
                Score.ScoreExternals: EXCLUDED.ScoreExternals,
            },
            where=(
                (Score.ScoreExternals + Score.ScoreInternals)
                < (EXCLUDED.ScoreInternals + EXCLUDED.ScoreExternals)
            ),
        ).execute()

        count = BacklogHistory.select().count()

        assert count == 1

    def test_check_trigger_ignores_lower_score(self):
        Score.insert(
            ScoreSerialNumber="1CR17CS001",
            ScoreSubjectCode="17CS56",
            ScoreInternals=56,
            ScoreExternals=22,
        ).execute()

        Score.insert(
            ScoreSerialNumber="1CR17CS001",
            ScoreSubjectCode="17CS56",
            ScoreInternals=56,
            ScoreExternals=20,
        ).on_conflict(
            conflict_target=[Score.ScoreSerialNumber, Score.ScoreSubjectCode],
            update={
                Score.ScoreInternals: EXCLUDED.ScoreInternals,
                Score.ScoreExternals: EXCLUDED.ScoreExternals,
            },
            where=(
                (Score.ScoreExternals + Score.ScoreInternals)
                < (EXCLUDED.ScoreInternals + EXCLUDED.ScoreExternals)
            ),
        ).execute()

        count = BacklogHistory.select().count()

        assert count == 0
