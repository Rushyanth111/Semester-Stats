from typing import List, Tuple

from sqlalchemy import func
from sqlalchemy.orm import Session

from ...database import BatchSchemeInfo, Score, Student
from ...reciepts import BatchAggregate, StudentTotalAggregate

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
    """Get all Batches

    Args:
        db (Session): SQLAlchemy Session

    Returns:
        List[int]: List of Batches
    """
    res = db.query(BatchSchemeInfo.Batch).all()
    batches = [x.Batch for x in res]
    return batches


def is_batch_exists(db: Session, batch: int) -> bool:
    """Check if Batch Exists

    Args:
        db (Session): SQLAlchemy Session
        batch (int): Batch Filter

    Returns:
        bool: True if Batch exists else False
    """
    equery = db.query(BatchSchemeInfo).filter(BatchSchemeInfo.Batch == batch)
    res = db.query(equery.exists()).scalar()
    return res


def get_batch_aggregate(
    db: Session, batch: int, dept: str = None
) -> List[Tuple[str, int]]:
    """Get Batch Complete Aggregate

    Args:
        db (Session): SQLAlchemy Session
        batch (int): Batch filter.
        dept (str, optional): Department Filter. Defaults to None.

    Returns:
        List[Tuple[str, int]]: List of Tuples that contain USN and their Aggregate.
    """
    res_score = (
        db.query(Score.Usn, func.sum(Score.Internals + Score.Externals))
        .join(Student)
        .filter(Student.Batch == batch)
        .group_by(Score.Usn)
    )

    if dept is not None:
        res_score = res_score.filter(Student.Department == dept)

    ret_list = []
    mean = 0
    for (usn, sum) in res_score:
        ret_list.append(StudentTotalAggregate(Usn=usn, Sum=sum))
        mean += sum

    mean = mean / len(ret_list)
    res = BatchAggregate(Mean=mean, StudentTotals=ret_list)

    return res
