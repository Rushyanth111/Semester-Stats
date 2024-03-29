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
        NoResultFound

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
        NoResultFound

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
    db: Session, batch: int, dept: str = None, thresh: int = 4
) -> List[StudentReport]:
    """Get Batch Detaine

    Args:
        db (Session): SQLAlchemy Session
        batch (int): Batch Filter
        dept (str, optional): Department Filter. Defaults to None.
        sem (int, optional): Semester Filter. Defaults to None.
        thresh (int, optional): Threshold for Detained. Defaults to 4.

    Raises:
        NoResultFound

    Returns:
        List[StudentReport]: List of Student Reports with Scores.
    """
    students, scores = _score_base(db, batch, dept)

    # Determine which is the most recent semester
    latest_semester = (
        scores.join(Subject)
        .group_by(Subject.Semester)
        .order_by(Subject.Semester.desc())
        .with_entities(Subject.Semester)
        .first()
    )[0]

    # According to Latest Semester, find out which do not have a Score in Latest
    # Semester.

    usns_not_in_latest = (
        scores.join(Student)
        .join(Subject)
        .group_by(Student.Usn)
        .with_entities(Student.Usn, func.max(Subject.Semester))
    ).all()

    avoid_usns = []
    for (stu, maxsem) in usns_not_in_latest:
        if maxsem < latest_semester:
            avoid_usns.append(stu)

    print("DEBUG:", usns_not_in_latest)

    usn = (
        scores.join(Subject)
        .filter(
            or_(
                Score.Internals + Score.Externals < Subject.MinTotal,
                Score.Externals < Subject.MinExt,
            ),
            Score.Usn.notin_(avoid_usns),
        )
        .group_by(Score.Usn)
        .having(func.count(Score.Usn) > thresh)
        .with_entities(Score.Usn)
    )

    scores = (
        scores.join(Subject)
        .filter(
            or_(
                Score.Internals + Score.Externals < Subject.MinTotal,
                Score.Externals < Subject.MinExt,
            )
        )
        .filter(Score.Usn.in_(usn))
    )

    return _adjoin_student_scores(students, scores)
