from semesterstat.api.common.reports import (
    StudentReport,
    SubjectReport,
    ScoreReport,
    Report,
)
import unittest


class ReportTest(unittest.TestCase):
    def test_student_report(self):
        rep = StudentReport(Usn="1CX15CS152", Name="Some Random Name")

        assert rep.Batch == 2015

        assert rep.Department == "CS"

    def test_subject_report(self):
        rep = SubjectReport(Code="17MATDIP41", Name="Mathematics 4 DIP")

        assert rep.Semester == 4

        assert rep.Scheme == 2017

        assert rep.Department == "XX"
