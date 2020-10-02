from .reciepts import (
    DepartmentReciept,
    ScoreMinimalReciept,
    ScoreReciept,
    StudentReciept,
    SubjectReciept,
)
from .reports import DepartmentReport, ScoreReport, StudentReport, SubjectReport


def convert_dept(report: DepartmentReport) -> DepartmentReciept:
    return DepartmentReciept.from_orm(report)


def convert_student(report: StudentReport) -> StudentReciept:
    return StudentReciept.from_orm(report)


def convert_subject(report: SubjectReport) -> SubjectReciept:
    return SubjectReciept.from_orm(report)


def convert_score(report: ScoreReport) -> ScoreReciept:
    return ScoreReciept.from_orm(report)


def convert_score_minimal(report: ScoreReport) -> ScoreMinimalReciept:
    return ScoreMinimalReciept.from_orm(report)
