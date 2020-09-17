from sqlalchemy.orm import Session
from ..database import BatchSchemeInfo


def get_scheme(db: Session, batch: int) -> int:
    return (
        db.query(BatchSchemeInfo.Scheme).filter(BatchSchemeInfo.Batch == batch).scalar()
    )
