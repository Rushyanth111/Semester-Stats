from typing import List, Optional, Union

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from semesterstat.common.reports import ScoreReport

from ..database import get_db

batch = APIRouter()

"""
/batch/Endpoint Details for Developer:

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

"""


@batch.get("/{batch}/summary", response_model=Union[List[ScoreReport], List[str]])
async def get_batch_summary(
    batch: int,
    department: Optional[str] = None,
    semester: Optional[int] = None,
    detain: Optional[bool] = False,
    listusn: Optional[bool] = False,
    backlogs: Optional[bool] = False,
    db: Session = Depends(get_db),
):
    pass


@batch.get("/{batch}/detail", response_model=Union[List[ScoreReport], List[str]])
async def get_batch_detail(
    batch: int,
    fcd: int,
    fc: int,
    sc: int,
    total: int,
    avoid: List[str] = Query(...),
    department: Optional[str] = None,
    semester: Optional[int] = None,
    detain: Optional[bool] = False,
    listusn: Optional[bool] = False,
    backlogs: Optional[bool] = False,
    db: Session = Depends(get_db),
):
    pass
