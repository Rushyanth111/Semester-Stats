"""
Purpose: Student Details Only:

- Details of Student, Name, Usn, Etc.

- Scores
    - Particular Semester.
    - Particular Subject
        - Range Of Subjects

    - Backlogs
"""
from sqlalchemy import func
from sqlalchemy.orm import Session, noload

from ..common.usn_extractor import get_usn_batch
from ..database.models import Score, Student, Subject
from ..reports import ScoreReport, StudentReport
from .common import get_scheme


def get_student(db: Session, usn: str):
    return StudentReport.from_orm(
        db.query(Student)
        .options(noload(Student.Scores))
        .filter(Student.Usn == usn)
        .first()
    )


def get_students(db: Session, batch: int = None, dept: str = None):
    res = db.query(Student.Usn)

    if batch is not None:
        res = res.filter(Student.Batch == batch)

    if dept is not None:
        res = res.filter(Student.Department == dept)

    usns = [student.Usn for student in res]

    return usns


def get_student_scores(db: Session, usn: str):
    res = db.query(Score).filter(Score.Usn == usn)
    return [ScoreReport.from_orm(x) for x in res]


def get_student_scores_by_semester(db: Session, usn: str, semester: int):
    res = (
        db.query(Score)
        .join(Subject)
        .filter(Score.Usn == usn, Subject.Semester == semester)
    )
    return [ScoreReport.from_orm(x) for x in res]


def get_student_subject(db: Session, usn: str, subcode: str):
    res = db.query(Score).filter(Score.Usn == usn, Score.SubjectCode == subcode).first()
    return ScoreReport.from_orm(res)


def get_student_backlogs(db: Session, usn: str, ext_thres: int, total_thres: int):
    pass


def is_student_exists(db: Session, usn: str) -> bool:
    res = db.query(Student).filter(Student.Usn == usn).one_or_none()

    if res is not None:
        return True

    return False


def put_student(db: Session, rep: StudentReport) -> None:

    ipt = Student(
        Usn=rep.Usn, Name=rep.Name, Batch=rep.Batch, Department=rep.Department
    )
    db.add(ipt)
    db.commit()


def update_student(db: Session, old: str, new: StudentReport) -> None:

    upd = db.query(Student).filter(Student.Usn == old).first()

    upd.Usn = new.Usn
    upd.Name = new.Name
    upd.Batch = new.Batch
    upd.Department = new.Department

    db.commit()


def get_student_score_credits(db: Session, usn: str, subcode: str) -> int:
    internals, externals, credits = (
        db.query(Score.Internals, Score.Externals, Subject.Credits)
        .join(Subject, Score.SubjectCode == Subject.Code)
        .filter(Score.Usn == usn, Score.SubjectCode == subcode)
        .first()
    )

    credits = ((internals + externals) // 10) * credits

    return credits


def get_student_sgpa(db: Session, usn: str, semester: int) -> float:
    batch = get_usn_batch(usn)
    scheme = get_scheme(db, batch)

    score_list = (
        db.query(Score.Internals, Score.Externals, Subject.Credits)
        .join(Subject)
        .filter(Score.Usn == usn, Subject.Semester == semester)
    )

    # Incase the Sum Credits are Zero.
    if score_list.count() == 0:
        return 0

    score_list = [
        ((internals + externals) // 10) * credits
        for internals, externals, credits in score_list
    ]

    score_total = sum(score_list)

    total_credits = (
        db.query(func.sum(Subject.Credits))
        .filter(Subject.Semester == semester, Subject.Scheme == scheme)
        .scalar()
    )

    return score_total / total_credits


def get_student_cgpa(db: Session, usn: str) -> None:
    sgpa_list = [get_student_sgpa(db, usn, sem) for sem in range(1, 9)]

    valid_count = 8 - sgpa_list.count(0)
    if valid_count == 0:
        return 0
    return sum(sgpa_list) / valid_count
