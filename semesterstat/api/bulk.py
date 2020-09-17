from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..common import ScoreReport, DepartmentReport, StudentReport, SubjectReport
from ..crud import (
    put_department_bulk,
    put_score_bulk,
    put_student_bulk,
    put_subject_bulk,
)
from ..database import get_db

bulk = APIRouter()

"""
The Bulk API Router handles the Bulk Transactions of the User, namely Updating Reports
and Adding new Reports.

"""


@bulk.post("/score", status_code=status.HTTP_201_CREATED)
async def score_bulk(reports: List[ScoreReport], db: Session = Depends(get_db)):
    put_score_bulk(db, reports)


@bulk.post("/dept", status_code=status.HTTP_201_CREATED)
async def dept_bulk(reports: List[DepartmentReport], db: Session = Depends(get_db)):
    put_department_bulk(db, reports)


@bulk.post("/student", status_code=status.HTTP_201_CREATED)
async def student_bulk(reports: List[StudentReport], db: Session = Depends(get_db)):
    put_student_bulk(db, reports)


@bulk.post("/subject", status_code=status.HTTP_201_CREATED)
async def subject_bulk(reports: List[SubjectReport], db: Session = Depends(get_db)):
    put_subject_bulk(db, reports)
