from typing import Any, List
from sqlalchemy.orm.session import Session
from ..database import Student, Subject

"""
Heirarchy of Batch Crud Operations:


get_batch
    |-> Department Filter   -> Detail or List Filters (Optional)
    |-> Semester Filter     -> Detail or List Filters (Optional)
    |-> Detained Filter     -> Detail or List Filters (Optional)
    |-> BackLog Filter      -> Detail or List Filters (Optional)
"""


def get_batch(db: Session, batch: int):
    return db.query(Student).filter(Student.Batch == batch)


def department_filter(query: Any, department: str):
    return query.filter(Student.Department == department)


def semester_filter(query: Any, semester: int):
    return query.filter(Subject.Semester == semester)


def detained_filter(query: Any):
    pass


def backlog_filter(query: Any):
    pass


def detail_filter(query: Any):
    pass


def listusn_filter(query: Any) -> List[str]:
    return query.with_entities(Student.Usn)
