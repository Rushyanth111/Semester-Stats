from ..database import Subject, BatchSchemeInfo, Student
from typing import List
from sqlalchemy.orm import Session


def get_subject_list(db: Session, semester: int, scheme: int) -> List[str]:
    # Returns the Subject List of a given Semester.
    return (
        db.query(Subject.Code)
        .filter(Subject.Semester == semester, Subject.Scheme == scheme)
        .all()
    )


def get_scheme(db: Session, batch: int) -> str:
    return (
        db.query(BatchSchemeInfo.Scheme).filter(BatchSchemeInfo.Batch == batch).first()
    )


def get_student_usn_list(db: Session, batch: int, department: str) -> List[str]:
    return (
        db.query(Student.Usn)
        .filter(Student.Batch == batch, Student.Department == department)
        .all()
    )
