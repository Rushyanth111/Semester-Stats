from operator import or_
from typing import List, Tuple, Any

from sqlalchemy.orm import Session, noload
from sqlalchemy import func, tuple_

from semesterstat.common.reports import ScoreReport, StudentReport

from ...database import BatchSchemeInfo, Score, Student, Subject
from ..common import get_scheme


"""
Heirarchy of Batch Crud Operations:


get_batch
    |-> Department Filter   -> List Filters (Optional)
    |-> Semester Filter     -> List Filters (Optional)
    |-> Detained Filter     -> List Filters (Optional)
    |-> BackLog Filter      -> List Filters (Optional)

Purpose:
- Obtain Scores As Per the Given Parameters.

Output:
- List[Student(List[Scores])]

"""


def _get_students_batch(db: Session, batch: int, dept: str = None):
    usns = db.query(Student).filter(Student.Batch == batch).options(noload("Scores"))

    if dept is not None:
        usns = usns.filter(Student.Department == dept)

    return usns


def _get_subjects_sem(db: Session, scheme: int, sem: int = None):
    subcodes = db.query(Subject).filter(Subject.Scheme == scheme)

    if sem is not None:
        subcodes = subcodes.filter(Subject.Semester == sem)

    return subcodes


def _adjoin_student_scores(students: Any, scores: Any) -> List[StudentReport]:
    students = [StudentReport.from_orm(x) for x in students]
    scores = [ScoreReport.from_orm(x) for x in scores]

    for student in students:
        for score in scores:
            if score.Usn == student.Usn:
                student.Scores.append(score)

    return [student for student in students if len(student.Scores) > 0]


def get_all_batch(db: Session) -> List[int]:
    res = db.query(BatchSchemeInfo.Batch).all()

    return [x.Batch for x in res]


def is_batch_exists(db: Session, batch: int):
    sb = db.query(BatchSchemeInfo).filter(BatchSchemeInfo.Batch == batch).exists()

    if db.query(sb).scalar() is False:
        return False

    return True


def _get_scores(
    db: Session, batch: int, dept: str = None, sem: int = None
) -> Tuple[Any, Any]:
    scheme = get_scheme(db, batch)
    usns = _get_students_batch(db, batch, dept)
    subcodes = _get_subjects_sem(db, scheme, sem)

    scores = (
        db.query(Score)
        .filter(Score.Usn.in_(usns.with_entities(Student.Usn).subquery()))
        .filter(Score.SubjectCode.in_(subcodes.with_entities(Subject.Code).subquery()))
    )

    return (scores, usns)


def get_batch_scores(
    db: Session, batch: int, dept: str = None, sem: int = None
) -> List[StudentReport]:
    scores, usns = _get_scores(db, batch, dept, sem)
    return _adjoin_student_scores(usns, scores)


def get_batch_backlog(
    db: Session, batch: int, dept: str = None, sem: int = None
) -> List[StudentReport]:
    scores, usns = _get_scores(db, batch, dept, sem)

    scores = scores.filter(
        or_(
            Score.Internals + Score.Externals < Subject.MinTotal,
            Score.Externals < Subject.MinExt,
        )
    )

    return _adjoin_student_scores(usns, scores)


def get_batch_detained_students(db: Session, batch: int, dept: str, thresh: int = 4):
    scheme = get_scheme(db, batch)
    usns = _get_students_batch(db, batch, dept)
    subcodes = _get_subjects_sem(db, scheme)

    backlog_scores = (
        db.query(Score.Usn, Score.SubjectCode)
        .join(Subject)
        .filter(Score.Usn.in_(usns.with_entities(Student.Usn).subquery()))
        .filter(Score.SubjectCode.in_(subcodes.with_entities(Subject.Code).subquery()))
        .filter(
            or_(
                Score.Internals + Score.Externals < Subject.MinTotal,
                Score.Externals < Subject.MinExt,
            )
        )
        .group_by(Score.Usn)
        .having(func.count(Score.SubjectCode) > thresh)
    )

    scores = db.query(Score).filter(
        tuple_(Score.Usn, Score.SubjectCode).in_(backlog_scores)
    )

    return _adjoin_student_scores(usns, scores)


def get_batch_aggregate(
    db: Session, batch: int, dept: str = None
) -> List[Tuple[str, int]]:
    res_score = (
        db.query(Score.Usn, func.sum(Score.Internals + Score.Externals))
        .join(Student)
        .filter(Student.Batch == batch)
        .group_by(Score.Usn)
    )

    if dept is not None:
        res_score = res_score.filter(Student.Department == dept)
    return [(x, y) for (x, y,) in res_score]
