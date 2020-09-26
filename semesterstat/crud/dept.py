"""
This Module Deals with Department Related Activities Only.

get_dept -> Get Details of a Department.
    - Filter Batch?
"""

from typing import List
from sqlalchemy.orm import Session, noload

from ..common import DepartmentReport, SubjectReport, StudentReport
from ..database import Department, Subject, Student


def get_all_dept(db: Session):
    res = db.query(Department.Code).all()

    return [x.Code for x in res]


def get_dept_by_code(db: Session, code: str) -> DepartmentReport:
    return DepartmentReport.from_orm(
        db.query(Department)
        .filter(Department.Code == code)
        .options(noload(Department.Students), noload(Department.Subjects))
        .first()
    )


def get_dept_by_name(db: Session, name: str) -> DepartmentReport:
    return DepartmentReport.from_orm(
        db.query(Department)
        .filter(Department.Name.like(name))
        .options(noload(Department.Students), noload(Department.Subjects))
        .first()
    )


def get_dept_subjects(
    db: Session, code: str, scheme: int = None
) -> List[SubjectReport]:
    res = db.query(Subject).filter(Subject.Department == code)

    if scheme is not None:
        res = res.filter(Subject.Scheme == scheme)

    return [SubjectReport.from_orm(x) for x in res]


def is_dept_exist(db: Session, code: str) -> bool:
    res = db.query(Department).filter(Department.Code == code).one_or_none()

    if res is not None:
        return True

    return False


def get_dept_students(db: Session, code: str) -> List[StudentReport]:
    res = db.query(Student).filter(Student.Department == code)

    return [StudentReport.from_orm(x) for x in res]


def put_department(db: Session, obj: DepartmentReport) -> None:
    ins = Department(Code=obj.Code, Name=obj.Name)
    db.add(ins)
    db.commit()


def update_department(db: Session, dept: str, new_obj: DepartmentReport) -> bool:

    upd = db.query(Department).filter(Department.Code == dept).first()

    upd.Code = new_obj.Code
    upd.Name = new_obj.Name

    db.commit()
