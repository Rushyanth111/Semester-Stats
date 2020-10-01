"""
This Module contains Funtions for the Document Generation Routes.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db

docs = APIRouter()


@docs.get("/{batch}/{dept}/{sem}/docx", deprecated=True)
def docgen(batch: int, dept: str, sem: int, db: Session = Depends(get_db)):
    pass


@docs.get("/{batch}/{dept}/{sem}/resa", deprecated=True)
def res_analysis(batch: int, dept: str, sem: int, db: Session = Depends(get_db)):
    pass
