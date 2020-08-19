from enum import Flag
from typing import List, Optional

from fastapi import APIRouter, Depends, status
from fastapi.params import Depends
from sqlalchemy.orm import Session, session
from starlette.responses import Response
from uvicorn.config import logger

from ..common import Report, ScoreReport
from ..database import Score, Student, Subject, get_db

batch = APIRouter()

"""
/batch/Endpoint Details for Developer:

- The Batch Endpoint is Strictly only for a given Batch.
- Available Mandatory Filters:
    - Department, Semester.
- Optional Filters.
    - detain: Bool = Only detained students returned.
    - listusn: Bool = Only USNs returned.
    - detail: Bool = Returns the Full List of Details, Students, USN, Scores, etc.
    - backlogs: Bool = Returns the List of Backlogs attained by students in the filter.

- Invalid Queries:
    - list and detail both True = Return a Bad Request.

"""


@batch.get("/{batch}/summary", response_model=ScoreReport)
async def get_batch_summary(
    batch: int,
    department: Optional[str] = None,
    semester: Optional[int] = None,
    detain: Optional[bool] = False,
    listusn: Optional[bool] = False,
    detail: Optional[bool] = False,
    backlogs: Optional[bool] = False,
    db: Session = Depends(get_db),
):
    if listusn is True and detail is True:
        # Cannot be detailed and Summary at the same time.
        return Response(status_code=status.HTTP_400_BAD_REQUEST)

    db.query()
