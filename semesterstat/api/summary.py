from fastapi import status
from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from semesterstat.reciepts import SummaryReciept

from ..crud.batch import is_batch_exists
from ..crud.dept import is_dept_exist
from ..crud.score import is_scores_exist
from ..crud.summary import get_summary
from ..database import get_db
from .exceptions import BatchDoesNotExist, DeptDoesNotExist, NoResultFoundForQuery

summary = APIRouter()


@summary.get(
    "/{batch}/{dept}/{sem}",
    status_code=status.HTTP_200_OK,
    response_model=SummaryReciept,
)
def summary_get(batch: int, dept: str, sem: int, db: Session = Depends(get_db)):
    if not is_batch_exists(db, batch):
        raise BatchDoesNotExist

    if not is_dept_exist(db, dept):
        raise DeptDoesNotExist

    if not is_scores_exist(db, batch, sem, dept):
        raise NoResultFoundForQuery

    res = get_summary(db, batch, dept, sem)

    return res
