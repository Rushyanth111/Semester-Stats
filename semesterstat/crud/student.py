"""
Purpose: Student Details Only:

- Details of Student, Name, Usn, Etc.

- Scores
    - Particular Semester.
    - Particular Subject
        - Range Of Subjects

    - Backlogs
"""
from sqlalchemy.orm import Session, noload
from ..database import Student, Score, Subject
from ..common import StudentReport, ScoreReport


def get_student(db: Session, usn: str):
    return StudentReport.from_orm(
        db.query(Student)
        .options(noload(Student.Scores))
        .filter(Student.Usn == usn)
        .first()
    )


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
    db.flush()


def update_student(db: Session, old: str, new: StudentReport) -> None:

    upd = db.query(Student).filter(Student.Usn == old).first()

    upd.Usn = new.Usn
    upd.Name = new.Name
    upd.Batch = new.Batch
    upd.Department = new.Department

    db.flush()
