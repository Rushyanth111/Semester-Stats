"""
Purpose: Student Details Only:

- Details of Student, Name, Usn, Etc.

- Scores
    - Particular Semester.
    - Particular Subject
        - Range Of Subjects

    - Backlogs
"""
from typing import List

from sqlalchemy import func, or_
from sqlalchemy.orm import Session, noload

from ..common.usn_extractor import get_usn_batch
from ..database.models import Score, Student, Subject
from ..reports import ScoreReport, StudentReport
from .common import get_scheme
from ..reciepts import StudentSummaryReciept


def get_student(db: Session, usn: str) -> StudentReport:
    """Obtain Student From USN

    Args:
        db (Session): SQLAlchemy Session
        usn (str): USN Code

    Raises:
        NoResultFound

    Returns:
        StudentReport: Student Object
    """
    res = (
        db.query(Student)
        .options(noload(Student.Scores))
        .filter(Student.Usn == usn)
        .one()
    )
    rep = StudentReport.from_orm(res)
    return rep


def get_students(db: Session, batch: int = None, dept: str = None) -> List[str]:
    """Obtain Student USNs

    Args:
        db (Session): SQLAlchemy Session.
        batch (int, optional): Batch of the Students. Defaults to None.
        dept (str, optional): Department of the Students. Defaults to None.

    Returns:
        List[str]: List of String of Student USN
    """
    res = db.query(Student.Usn)

    if batch is not None:
        res = res.filter(Student.Batch == batch)

    if dept is not None:
        res = res.filter(Student.Department == dept)

    usns = [student.Usn for student in res]

    return usns


def get_student_scores(db: Session, usn: str, sem: int = None) -> List[ScoreReport]:
    """Obtain All of Scores Linked to USN

    Args:
        db (Session): SQLAlchemy Session
        usn (str): USN Code
        sem (int, None): Particular Semester for Scores. Defaults to None

    Returns:
        List[ScoreReport]: List of Scores.
    """
    res = db.query(Score).filter(Score.Usn == usn)

    if sem is not None:
        res = res.join(Subject).filter(Subject.Semester == sem)

    list_scores = [ScoreReport.from_orm(x) for x in res]

    return list_scores


def get_student_subject(db: Session, usn: str, subcode: str) -> ScoreReport:
    """Get One Subject of a Student

    Args:
        db (Session): SQLAlchemy Session
        usn (str): USN code
        subcode (str): Subject Code

    Raises:
        NoResultFound

    Returns:
        ScoreReport: Score Object Containing Details
    """
    res = db.query(Score).filter(Score.Usn == usn, Score.SubjectCode == subcode).one()
    rep = ScoreReport.from_orm(res)
    return rep


def get_student_backlogs(db: Session, usn: str, sem: int = None) -> List[ScoreReport]:
    """Get Student Backlogs

    Args:
        db (Session): SQLAlchemy Session
        usn (str): USN Code
        sem (int, optional): Semester. Defaults to None.

    Returns:
        List[ScoreReport]: List of Score Reports
    """
    res = (
        db.query(Score)
        .join(Subject)
        .filter(
            Score.Usn == usn,
            or_(
                Score.Externals < Subject.MinExt,
                Score.Externals + Score.Internals < Subject.MinTotal,
            ),
        )
    )

    if sem is not None:
        res = res.filter(Subject.Semester == sem)

    scores = [ScoreReport.from_orm(x) for x in res]

    return scores


def is_student_exists(db: Session, usn: str) -> bool:
    """Check if Student Exists

    Args:
        db (Session): SQLAlchemy Session.
        usn (str): USN Code

    Returns:
        bool: True if Present else False.
    """
    equery = db.query(Student).filter(Student.Usn == usn)
    res = db.query(equery.exists()).scalar()
    return res


def put_student(db: Session, rep: StudentReport) -> None:
    """Insert Student

    Args:
        db (Session): SQLAlchemy Session
        rep (StudentReport): Student Report, For New Student

    Raises:
        IntegrityError
    """
    ipt = Student(
        Usn=rep.Usn, Name=rep.Name, Batch=rep.Batch, Department=rep.Department
    )
    db.add(ipt)
    db.commit()


def update_student(db: Session, old: str, new: StudentReport) -> None:
    """Update Student

    Args:
        db (Session): SQLAlchemy Session
        old (str): Old USN Code
        new (StudentReport): New Student Information

    Raises:
        IntegrityError
    """
    upd = db.query(Student).filter(Student.Usn == old).first()

    upd.Usn = new.Usn
    upd.Name = new.Name
    upd.Batch = new.Batch
    upd.Department = new.Department

    db.commit()


def get_student_score_credits(db: Session, usn: str, subcode: str) -> int:
    """Get Score Credits

    Args:
        db (Session): SQLAlchemy Session
        usn (str): USN Code
        subcode (str): Subject Code

    Returns:
        int: Final Credits Earned
    """
    internals, externals, credits = (
        db.query(Score.Internals, Score.Externals, Subject.Credits)
        .join(Subject, Score.SubjectCode == Subject.Code)
        .filter(Score.Usn == usn, Score.SubjectCode == subcode)
        .first()
    )

    final_score = ((internals + externals) // 10) * credits

    return final_score


def get_student_sgpa(db: Session, usn: str, semester: int) -> float:
    """SGPA Of a student, For a Particular Semester

    Args:
        db (Session): SQLAlchemy Session.
        usn (str): USN Code
        semester (int): Semester for SGPA

    Returns:
        float: SGPA for Given Semester
    """
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


def get_student_cgpa(db: Session, usn: str) -> float:
    """CGPA; Average of All CGPA of a Student

    Args:
        db (Session): SQLAlchemy Session
        usn (str): USN Code

    Returns:
        [float]: CGPA for a Student
    """
    sgpa_list = [get_student_sgpa(db, usn, sem) for sem in range(1, 9)]

    valid_count = 8 - sgpa_list.count(0)
    if valid_count == 0:
        return 0
    return sum(sgpa_list) / valid_count


def get_student_summary(db: Session, usn: str) -> None:
    """Utility Function that Combines the CGPA and SGPA Results.

    Args:
        db(Session): SQLALchemy Session
        usn (str): USN Code.

    Returns:
    """

    sgpa_list = [get_student_sgpa(db, usn, sem) for sem in range(1, 9)]

    valid_count = 8 - sgpa_list.count(0)
    if valid_count == 0:
        return 0

    cgpa = sum(sgpa_list) / valid_count

    res = StudentSummaryReciept(
        Usn=usn, CGPA=cgpa, SGPA={k: v for k, v in zip(range(1, 9), sgpa_list)}
    )

    return res
