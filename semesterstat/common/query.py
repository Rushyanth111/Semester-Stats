from ..database import Subject, BatchSchemeInfo, Student
from typing import List


def get_subject_list(semester: int, scheme: int) -> List[str]:
    # Returns the Subject List of a given Semester.
    return [
        sub
        for sub in Subject.select(Subject.Code).where(
            (Subject.Scheme == scheme) & (Subject.Semester == semester)
        )
    ]


def get_scheme(batch: int) -> str:
    return (
        BatchSchemeInfo.select(BatchSchemeInfo.Scheme)
        .where((BatchSchemeInfo.Batch == batch))
        .execute()
    )


def get_student_usn_list(batch: int, department: str) -> List[str]:
    return [
        student.Usn
        for student in Student.select(Student.Usn).where(
            (Student.Department == department) & (Student.Batch == batch)
        )
    ]
