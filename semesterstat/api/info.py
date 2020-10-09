"""
Information Route, To get a lot of the Information Required.

"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from ..crud.common import get_scheme
from ..database import get_db

info = APIRouter()


@info.get("/scheme/{batch}", response_model=int, status_code=status.HTTP_200_OK)
def info_get_batch(batch: int, db: Session = Depends(get_db)):
    try:
        res = get_scheme(db, batch)
        return res
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Batch Doesn't Exist"
        )
