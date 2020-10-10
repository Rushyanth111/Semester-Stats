from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from semesterstat.database.models import Score

from .student import get_students
from .subject import get_subjects


def is_scores_exist(db: Session, batch: int, sem: int, dept: str = None):
    try:
        subcodes = get_subjects(db, batch, dept, sem)
    except NoResultFound:
        subcodes = []

    students = get_students(db, batch, dept)

    if len(subcodes) == 0 or len(students) == 0:
        return False

    equery = db.query(Score).filter(
        Score.Usn.in_(students), Score.SubjectCode.in_(subcodes)
    )

    res = db.query(equery.exists()).scalar()

    return res
