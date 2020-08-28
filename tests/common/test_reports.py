from semesterstat.common import (
    StudentReport,
    SubjectReport,
)


def test_student_report():
    rep = StudentReport(Usn="1CR15CS401", Name="Some Random Name")
    assert rep.Batch == 2015
    assert rep.Department == "CS"


def test_subject_report():
    rep = SubjectReport(Code="17MATDIP41", Name="Mathematics 4 DIP")
    assert rep.Semester == 4
    assert rep.Scheme == 2017
    assert rep.Department == "XX"
