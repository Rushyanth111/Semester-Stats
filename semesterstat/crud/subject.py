"""
Subject Crud:

Purpose: Get Subject, Update Subject, And Put Subject, Nothing More.

"""
from typing import List

from sqlalchemy import or_
from sqlalchemy.orm import Session

from ..database.models import Subject
from ..reports import SubjectReport
from .common import get_scheme


def get_subject(db: Session, subcode: str) -> SubjectReport:
    """Get Subject From Code

    Args:
        db (Session): SQLAlchemy Session.
        subcode (str): Subject Code.

    Raises:
        NoResultFound

    Returns:
        SubjectReport: Details Of the Requested Subject.
    """
    res = db.query(Subject).filter(Subject.Code == subcode).one()
    rep = SubjectReport.from_orm(res)
    return rep


def put_subject(db: Session, sub: SubjectReport) -> None:
    """Add a Subject to the Database

    Args:
        db (Session): SQLAlchemy Session.
        sub (SubjectReport): Subject Report Object.

    Raises:
        IntegrityError
    """
    ipt = Subject(
        Code=sub.Code,
        Name=sub.Name,
        Semester=sub.Semester,
        Scheme=sub.Scheme,
        Department=sub.Department,
    )
    db.add(ipt)
    db.commit()


def update_subject(db: Session, old_sub: str, new_sub: SubjectReport) -> None:
    """Update a Subject

    Args:
        db (Session): SQLAlchemy Session.
        old_sub (str): Old Subject Code.
        new_sub (SubjectReport): Subject Details to Change

    Raises:
        IntegrityError
    """
    upd = db.query(Subject).filter(Subject.Code == old_sub).first()

    upd.Code = new_sub.Code
    upd.Name = new_sub.Name
    upd.Semester = new_sub.Semester
    upd.Scheme = new_sub.Scheme
    upd.Department = new_sub.Department

    db.commit()


def is_subject_exist(db: Session, subcode: str) -> bool:
    """Checks if Subject Exists.

    Args:
        db (Session): SQLAlchemy Session.
        subcode (str): Subject Code.

    Returns:
        bool: True if Present, Else False.
    """
    equery = db.query(Subject).filter(Subject.Code == subcode)
    res = db.query(equery.exists()).scalar()

    return res


def get_subjects(
    db: Session, batch: int = None, dept: str = None, sem: int = None
) -> List[str]:
    """Obtains a List of Subjects According to Optional Params

    Args:
        db (Session): SQLAlchemy Session.
        batch (int, optional): Batch that Attended That Subject. Defaults to None.
        dept (str, optional): Department of the Subject(Includes "XX" By default).
             Defaults to None.
        sem (int, optional): Semester Of the Subject. Defaults to None.

    Raises:
        NoResultFound

    Returns:
        List[str]: List of the Subject Codes Searched.
    """

    res = db.query(Subject)

    if batch is not None:
        scheme = get_scheme(db, batch)

        if scheme is None:
            return []
        res = res.filter(Subject.Scheme == scheme)

    if dept is not None:
        # Fixing Fetch From Common Department Bug:
        if dept != "XX":
            res = res.filter(
                or_(Subject.Department == dept, Subject.Department == "XX")
            )
        else:
            res = res.filter(Subject.Department == "XX")

    if sem is not None:
        res = res.filter(Subject.Semester == sem)

    subcodes = [sub.Code for sub in res]
    return subcodes
