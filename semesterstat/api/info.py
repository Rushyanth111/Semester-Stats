"""
Information Route, To get a lot of the Information Required.

"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..crud.common import get_scheme
from ..database import get_db

info = APIRouter()


@info.get("/scheme/{batch}", response_model=int)
def info_get_batch(batch: int, db: Session = Depends(get_db)):
    return get_scheme(db, batch)
