from sqlalchemy.orm import Session

from ..database.models import BatchSchemeInfo


def get_scheme(db: Session, batch: int) -> int:
    """Obtain Scheme of Given Batch.

    Args:
        db (Session): SQLAlchemy Database.
        batch (int): Batch to be Found.

    Raises:
        NoResultFound

    Returns:
        int: The Scheme of the Given Batch.
    """
    res = db.query(BatchSchemeInfo.Scheme).filter(BatchSchemeInfo.Batch == batch).one()
    final_res = res.Scheme
    return final_res
