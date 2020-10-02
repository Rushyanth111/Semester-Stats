"""
Subject Crud:

Purpose: Get Subject, Update Subject, And Put Subject, Nothing More.

"""
from typing import List

from sqlalchemy.orm import Session

from ..common import SubjectReport
from ..database import Subject
from .common import get_scheme


def get_subject(db: Session, subcode: str):
    res = db.query(Subject).filter(Subject.Code == subcode).first()
    return SubjectReport.from_orm(res)


def put_subject(db: Session, sub: SubjectReport):
    ipt = Subject(
        Code=sub.Code,
        Name=sub.Name,
        Semester=sub.Semester,
        Scheme=sub.Scheme,
        Department=sub.Department,
    )
    db.add(ipt)
    db.commit()


def update_subject(db: Session, old_sub: str, new_sub: SubjectReport):

    upd = db.query(Subject).filter(Subject.Code == old_sub).first()

    upd.Code = new_sub.Code
    upd.Name = new_sub.Name
    upd.Semester = new_sub.Semester
    upd.Scheme = new_sub.Scheme
    upd.Department = new_sub.Department

    db.commit()


def is_subject_exist(db: Session, subcode: str) -> bool:

    res = db.query(Subject).filter(Subject.Code == subcode).one_or_none()

    if res is not None:
        return True
    return False


def is_subjects_exists(db: Session, subcodes: List[str]) -> bool:
    for subcode in subcodes:
        sub_res = db.query(Subject).filter(Subject.Code == subcode).exists()
        res = db.query(sub_res).scalar()

        if res is False:
            return False

    return True


def get_subject_batch_sem_list(db: Session, batch: int, sem: int = None) -> List[str]:
    scheme = get_scheme(db, batch)
    res = db.query(Subject).filter(Subject.Scheme == scheme)

    if sem is not None:
        res = res.filter(Subject.Semester == sem)

    return [sub.Code for sub in res]
