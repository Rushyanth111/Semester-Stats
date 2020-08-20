from semesterstat.common import (
    StudentReport,
    SubjectReport,
)
import unittest


class ReportTest(unittest.TestCase):
    def test_student_report(self):
        rep = StudentReport(Usn="1CR15CS401", Name="Some Random Name")
        self.assertEqual(rep.Batch, 2015, "Batch is Not Correct")
        self.assertEqual(rep.Department, "CS", "Department is not Correct")

    def test_subject_report(self):
        rep = SubjectReport(Code="17MATDIP41", Name="Mathematics 4 DIP")

        self.assertEqual(rep.Semester, 4, "Semester is not Correct.")
        self.assertEqual(rep.Scheme, 2017, "Scheme is not Correct")
        self.assertEqual(rep.Department, "XX", "Department is not Correct")
