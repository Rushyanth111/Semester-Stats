"""
This Module Deals with Department Related Activities Only.

get_dept -> Get Details of a Department.
    - Filter Batch?
"""

from typing import List

from sqlalchemy.orm import Session

from ..database.models import Department
from ..reports import DepartmentReport


def get_all_dept(db: Session) -> List[str]:
    """Obtain all Departments Code.

    Args:
        db (Session): [description]

    Returns:
        List[str]: List of String of Subject Codes.
    """
    res = db.query(Department.Code).all()
    deptcodes = [x.Code for x in res]

    return deptcodes


def get_dept_by_code(db: Session, code: str) -> DepartmentReport:
    """Obtain Department By Department Code.

    Args:
        db (Session): SQLAlchemy Session
        code (str): Department Code.

    Raises:
        NoResultFound: No Result of the Type Found.

    Returns:
        DepartmentReport: Department Report.
    """
    res = db.query(Department).filter(Department.Code == code).one()
    rep = DepartmentReport.from_orm(res)
    return rep


def is_dept_exist(db: Session, code: str) -> bool:
    """Does the Department Exist.

    Args:
        db (Session): SQLAlchemy Session
        code (str): Department String

    Returns:
        bool: True if the Department exists, else False.
    """
    equery = db.query(Department.Code).filter(Department.Code == code)
    res = db.query(equery.exists()).scalar()
    return res


def put_department(db: Session, obj: DepartmentReport) -> None:
    """Insert a Given Department

    Args:
        db (Session): SQLAlchemy Session
        obj (DepartmentReport): Department Report with the New Department Details.

    Raises:
        IntegrityError
    """
    ins = Department(Code=obj.Code, Name=obj.Name)
    db.add(ins)
    db.commit()


def update_department(db: Session, dept: str, new_obj: DepartmentReport) -> None:
    """Update a Given Department

    Args:
        db (Session): SQLAlchemy Session
        dept (str): Department Code To Change.
        new_obj (DepartmentReport): Department Report with the New Department Details.

    Raises:
        IntegrityError
    """
    upd = db.query(Department).filter(Department.Code == dept).first()

    upd.Code = new_obj.Code
    upd.Name = new_obj.Name

    db.commit()
