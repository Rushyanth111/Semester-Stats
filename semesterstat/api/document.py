"""
This Module contains Funtions for the Document Generation Routes.
"""

from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from ..crud.batch import is_batch_exists
from ..crud.dept import is_dept_exist
from ..crud.score import is_scores_exist
from ..database import get_db
from ..docgen import get_docx
from .exceptions import BatchDoesNotExist, DeptDoesNotExist, NoResultFoundForQuery

docs = APIRouter()


@docs.get("/{batch}/{dept}/{sem}/docx")
def docgen(batch: int, dept: str, sem: int, db: Session = Depends(get_db)):

    if not is_batch_exists(db, batch):
        raise BatchDoesNotExist
    if not is_dept_exist(db, dept):
        raise DeptDoesNotExist
    if not is_scores_exist(db, batch, sem, dept):
        raise NoResultFoundForQuery

    return StreamingResponse(
        get_docx(db, batch, dept, sem),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",  # noqa
    )


@docs.get("/{batch}/{dept}/{sem}/resa", deprecated=True)
def res_analysis(batch: int, dept: str, sem: int, db: Session = Depends(get_db)):
    pass
