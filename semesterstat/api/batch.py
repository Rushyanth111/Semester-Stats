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


from typing import List, Tuple

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..crud.batch import (
    get_all_batch,
    get_batch_aggregate,
    get_batch_backlog,
    get_batch_detained,
    get_batch_scores,
    get_batch_scores_sum,
    is_batch_exists,
)
from ..database import get_db
from ..reciepts import BatchScoreSumReciept, StudentScoreReciept
from .exceptions import BatchDoesNotExist

batch = APIRouter()


def common_batch_verify(batch: int, db: Session = Depends(get_db)) -> int:
    if not is_batch_exists(db, batch):
        raise BatchDoesNotExist
    return batch


@batch.get(
    "/",
    responses={
        200: {
            "content": {
                "application/json": {
                    "example": [2015, 2016, 2017, 2018],
                    "schema": {
                        "title": "BatchListReciept",
                        "type": "array",
                        "items": {"type": "integer"},
                    },
                }
            }
        },
    },
)
async def batch_get_all(db: Session = Depends(get_db)):
    return get_all_batch(db)


@batch.get("/{batch}/scores", response_model=List[StudentScoreReciept])
async def batch_get_scores(
    batch: int = Depends(common_batch_verify),
    dept: str = None,
    sem: int = None,
    db: Session = Depends(get_db),
):
    res = get_batch_scores(db, batch, dept, sem)
    ret = [StudentScoreReciept.from_orm(x) for x in res]
    return ret


@batch.get("/{batch}/detained", response_model=List[StudentScoreReciept])
async def batch_get_detained(
    batch: int = Depends(common_batch_verify),
    dept: str = None,
    thresh: int = None,
    db: Session = Depends(get_db),
):
    if thresh is None:
        thresh = 4
    res = get_batch_detained(db, batch, dept, thresh)
    ret = [StudentScoreReciept.from_orm(x) for x in res]
    return ret


@batch.get("/{batch}/backlogs", response_model=List[StudentScoreReciept])
async def batch_get_backlogs(
    batch: int = Depends(common_batch_verify),
    dept: str = None,
    sem: int = None,
    db: Session = Depends(get_db),
):
    res = get_batch_backlog(db, batch, dept, sem)
    ret = [StudentScoreReciept.from_orm(x) for x in res]
    return ret


@batch.get("/{batch}/aggregate", response_model=List[Tuple[str, int]])
async def batch_get_aggregate(
    batch: int = Depends(common_batch_verify),
    dept: str = None,
    db: Session = Depends(get_db),
):
    return get_batch_aggregate(db, batch, dept)


@batch.get("/{batch}/summary", response_model=List[BatchScoreSumReciept])
async def batch_get_scoresum(
    batch: int = Depends(common_batch_verify),
    dept: str = None,
    db: Session = Depends(get_db),
):
    return get_batch_scores_sum(db, batch, dept)
