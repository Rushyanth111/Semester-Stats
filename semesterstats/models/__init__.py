from .BasicModels import (
    db,
    DepartmentDetails,
    BatchSchemeInfo,
    StudentDetails,
    SubjectDetails,
    SubjectScore,
    BacklogSubjectScore,
    ParsedTable,
    TeacherDetails,
    TeacherTaughtDetails,
)

from .DepartmentConstants import DepartmentCodeDictionary

__all__ = [
    "db",
    "DepartmentDetails",
    "BatchSchemeInfo",
    "StudentDetails",
    "SubjectDetails",
    "SubjectScore",
    "BacklogSubjectScore",
    "ParsedTable",
    "TeacherDetails",
    "TeacherTaughtDetails",
    "DepartmentCodeDictionary",
]
