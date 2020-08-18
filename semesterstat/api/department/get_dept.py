from fastapi.params import Depends
from fastapi import APIRouter, Response, status
from sqlalchemy.orm.session import Session
from ..common.reciept import DeparmentReceipt
from ...database import get_db, Department

get_dept = APIRouter()


@get_dept.get("/{department}", response_model=DeparmentReceipt)
def get_department(department: str, db: Session = Depends(get_db)):
    res = db.query(Department).filter(Department.Code == department).one_or_none()
    if res is None:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        return DeparmentReceipt(Code=res.Code, Name=res.Name)
