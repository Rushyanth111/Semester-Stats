from semesterstat.crud.batch import get_batch_scores
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic.main import BaseModel
from sqlalchemy.orm import Session

from semesterstat.common import StudentReport

from ..crud import (
    get_batch_aggregate,
    get_batch_detained_students,
    get_batch_students,
    get_batch_students_usn,
    get_scheme,
    is_batch_exists,
)
from ..database import get_db

batch = APIRouter()

"""
/batch/ Endpoint Details for Developer:

- The Batch Endpoint is Strictly only for a given Batch.
- Available Mandatory Filters:
    - Department, Semester.
- Optional Filters.
    - detain: Bool = Only detained students returned.
    - listusn: Bool = Only USNs returned.
    - backlogs: Bool = Returns the List of Backlogs attained by students in the filter.

- Invalid Queries:
    - list and detail both True = Return a Bad Request.

- Detail Endpoint:
    - Takes in Mandatory FCD, FC, SC, Total, Avoid Subject
    for Further Calculation.

    - Expensive.

- Endpoint Details:

POST {batch}/search
    - Note: Reserved to ensure that Other Operations can be streamlined.
    - Above Details

"""


class ListOnlyOutput(BaseModel):
    Usn: List[str]


def common_batch_verify(batch: int, db: Session = Depends(get_db)):
    if not is_batch_exists(db, batch):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Batch does not Exist."
        )
    return batch


@batch.get(
    "/{batch}", response_model=List[StudentReport], response_model_exclude_unset=True
)
async def batch_get_students(
    batch: int = Depends(common_batch_verify),
    dept: str = None,
    db: Session = Depends(get_db),
):
    return get_batch_students(db, batch, dept)


@batch.get("/{batch}/scores", response_model=List[StudentReport])
async def batch_get_scores(
    batch: int = Depends(common_batch_verify),
    dept: str = None,
    sem: int = None,
    db: Session = Depends(get_db),
):
    return get_batch_scores(db, batch, dept, sem)


@batch.get("/{batch}/usns", response_model=List[str])
async def batch_get_student_usns(
    batch: int = Depends(common_batch_verify),
    dept: str = None,
    db: Session = Depends(get_db),
):
    return get_batch_students_usn(db, batch, dept)


@batch.get("/{batch}/scheme")
async def batch_get_scheme(
    batch: int = Depends(common_batch_verify), db: Session = Depends(get_db)
):
    return get_scheme(db, batch)


@batch.get("/{batch}/detained", deprecated=True)
async def batch_get_detained(
    batch: int, dept: str = None, db: Session = Depends(get_db)
):
    return get_batch_detained_students(db, batch, dept)


@batch.get("/{batch}/backlogs", deprecated=True)
async def batch_get_backlogs(
    batch: int = Depends(common_batch_verify),
    dept: str = None,
    sem: int = None,
    db: Session = Depends(get_db),
):
    pass


@batch.get("/{batch}/aggregate")
async def batch_get_aggregate(
    batch: int = Depends(common_batch_verify),
    dept: str = None,
    db: Session = Depends(get_db),
):
    return get_batch_aggregate(db, batch, dept)


@batch.post("/{batch}/search", deprecated=True)
async def batch_search(
    batch: int = Depends(common_batch_verify), db: Session = Depends(get_db),
):
    pass
