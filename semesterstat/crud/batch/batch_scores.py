"""
Rationale for Having a different query for each of these:

They are very much tied to the query base here.
"""


from typing import Any, List

from sqlalchemy import func, or_
from sqlalchemy.orm import Session, noload

from ...database.models import Score, Student, Subject
from ...reports import ScoreReport, StudentReport
from ..common import get_scheme


def _adjoin_student_scores(students: Any, scores: Any) -> List[StudentReport]:
    students = [StudentReport.from_orm(x) for x in students]
    scores = [ScoreReport.from_orm(x) for x in scores]
    for student in students:
        for score in scores:
            if score.Usn == student.Usn:
                student.Scores.append(score)

    student_scores = [student for student in students if len(student.Scores) > 0]

    return student_scores


def _score_base(db: Session, batch: int, dept: str = None, sem: int = None):
    scheme = get_scheme(db, batch)
    usns = db.query(Student.Usn).filter(Student.Batch == batch)
    students = (
        db.query(Student).filter(Student.Batch == batch).options(noload("Scores"))
    )

    if dept is not None:
        usns = usns.filter(Student.Department == dept)
        students = students.filter(Student.Department == dept)

    subcodes = db.query(Subject.Code).filter(Subject.Scheme == scheme)

    if sem is not None:
        subcodes = subcodes.filter(Subject.Semester == sem)

    scores = db.query(Score).filter(
        Score.Usn.in_(usns), Score.SubjectCode.in_(subcodes)
    )

    return (students, scores)


def get_batch_scores(
    db: Session, batch: int, dept: str = None, sem: int = None
) -> List[StudentReport]:
    """Get Batch Scores

    Args:
        db (Session): SQLAlchemy Session
        batch (int): Batch
        dept (str, optional): Department Filter. Defaults to None.
        sem (int, optional): Semester Filter. Defaults to None.

    Raises:
        IntegrityError

    Returns:
        List[StudentReport]: List of Student Reports with Scores.
    """
    students, scores = _score_base(db, batch, dept, sem)

    return _adjoin_student_scores(students, scores)


def get_batch_backlog(
    db: Session, batch: int, dept: str = None, sem: int = None
) -> List[StudentReport]:
    """Get Batch Backlog

    Args:
        db (Session): SQLAlchemy Session
        batch (int): Batch
        dept (str, optional): Department Filter. Defaults to None.
        sem (int, optional): Semester Filter. Defaults to None.

    Raises:
        IntegrityError

    Returns:
        List[StudentReport]: List of Student Reports with Scores.
    """
    students, scores = _score_base(db, batch, dept, sem)

    scores = scores.join(Subject).filter(
        or_(
            Score.Internals + Score.Externals < Subject.MinTotal,
            Score.Externals < Subject.MinExt,
        )
    )

    return _adjoin_student_scores(students, scores)


def get_batch_detained(
    db: Session, batch: int, dept: str = None, sem: int = None, thresh: int = 4
) -> List[StudentReport]:
    """Get Batch Detaine

    Args:
        db (Session): SQLAlchemy Session
        batch (int): Batch Filter
        dept (str, optional): Department Filter. Defaults to None.
        sem (int, optional): Semester Filter. Defaults to None.
        thresh (int, optional): Threshold for Detained. Defaults to 4.

    Raises:
        IntegrityError

    Returns:
        List[StudentReport]: List of Student Reports with Scores.
    """
    students, scores = _score_base(db, batch, dept, sem)

    scores = (
        scores.join(Subject)
        .filter(
            or_(
                Score.Internals + Score.Externals < Subject.MinTotal,
                Score.Externals < Subject.MinExt,
            )
        )
        .group_by(Score.Usn)
        .having(func.count(Score.Usn) > thresh)
    )

    return _adjoin_student_scores(students, scores)
