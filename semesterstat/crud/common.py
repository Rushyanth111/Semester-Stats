from sqlalchemy.orm import Session
from ..database import BatchSchemeInfo


def get_scheme(db: Session, batch: int) -> int:
    res = (
        db.query(BatchSchemeInfo.Scheme).filter(BatchSchemeInfo.Batch == batch).scalar()
    )

    return res
