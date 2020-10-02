"""
This Module contains Funtions for the Document Generation Routes.
"""

from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from ..crud import is_batch_exists, is_dept_exist
from ..database import get_db
from ..docgen import get_docx

docs = APIRouter()


@docs.get("/{batch}/{dept}/{sem}/docx")
def docgen(batch: int, dept: str, sem: int, db: Session = Depends(get_db)):

    if not is_batch_exists(db, batch):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Batch does not Exist."
        )

    if not is_dept_exist(db, batch):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Dept does not Exist."
        )

    return StreamingResponse(
        get_docx(db, batch, dept, sem),
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",  # noqa
    )


@docs.get("/{batch}/{dept}/{sem}/resa", deprecated=True)
def res_analysis(batch: int, dept: str, sem: int, db: Session = Depends(get_db)):
    pass
