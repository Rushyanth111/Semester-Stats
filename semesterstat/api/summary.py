from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from ..database import get_db

summary = APIRouter()


@summary.get("/{batch}/{dept}/{sem}", deprecated=True)
def get_summary(batch: int, dept: str, sem: int, db: Session = Depends(get_db)):
    return None
