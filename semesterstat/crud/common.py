from typing import Optional

from sqlalchemy.orm import Session

from ..database.models import BatchSchemeInfo


def get_scheme(db: Session, batch: int) -> Optional[int]:
    res = (
        db.query(BatchSchemeInfo.Scheme).filter(BatchSchemeInfo.Batch == batch).scalar()
    )

    return res
