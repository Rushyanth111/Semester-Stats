from semesterstat.api.common.reports import (
    StudentReport,
    SubjectReport,
)
import unittest
import importlib_resources as pk
from test import TestMaterial
import csv


class ReportTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        material = pk.read_text(TestMaterial, "Usn.csv").splitlines()
        cls.materal = csv.reader(material, skipinitialspace=True)

    def test_student_report(self):

        for usn, batch, dept, dip in self.materal:
            batch = int(batch)
            rep = StudentReport(Usn=usn, Name="Some Random Name")
            self.assertEqual(rep.Batch, batch, "Batch is Not Correct")
            self.assertEqual(rep.Department, dept, "Department is not Correct")

    def test_subject_report(self):
        rep = SubjectReport(Code="17MATDIP41", Name="Mathematics 4 DIP")

        self.assertEqual(rep.Semester, 4, "Semester is not Correct.")
        self.assertEqual(rep.Scheme, 2017, "Scheme is not Correct")
        self.assertEqual(rep.Department, "XX", "Department is not Correct")
