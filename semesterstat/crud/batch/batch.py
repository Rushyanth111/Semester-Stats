from typing import List, Tuple

from sqlalchemy import func
from sqlalchemy.orm import Session

from ...database import BatchSchemeInfo, Score, Student

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


def get_all_batch(db: Session) -> List[int]:
    res = db.query(BatchSchemeInfo.Batch).all()

    return [x.Batch for x in res]


def is_batch_exists(db: Session, batch: int):
    sb = db.query(BatchSchemeInfo).filter(BatchSchemeInfo.Batch == batch).exists()

    if db.query(sb).scalar() is False:
        return False

    return True


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
