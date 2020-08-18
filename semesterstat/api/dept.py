from fastapi import APIRouter, Response, status
from fastapi.params import Depends
from sqlalchemy.orm.session import Session

from ..database import Department, get_db
from ..common import DeparmentReceipt

dept = APIRouter()


@dept.get("/{department}", response_model=DeparmentReceipt)
def get_department(department: str, db: Session = Depends(get_db)):
    res = db.query(Department).filter(Department.Code == department).one_or_none()
    if res is None:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        return DeparmentReceipt(Code=res.Code, Name=res.Name)
