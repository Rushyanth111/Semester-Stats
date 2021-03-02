from typing import List

from sqlalchemy.orm import Session

from ...database import BatchSchemeInfo

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
