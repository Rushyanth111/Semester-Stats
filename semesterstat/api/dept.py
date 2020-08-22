from fastapi import APIRouter, Response, status
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import noload
from typing import Union

from ..database import Department, get_db
from ..common import DepartmentReport

dept = APIRouter()


@dept.get(
    "/{department}",
    response_model=DepartmentReport,
    response_model_include={"Code", "Name"},
)
def get_department(department: str, db: Session = Depends(get_db)):
    res = (
        db.query(Department)
        .options(noload("Subjects"))
        .options(noload("Students"))
        .filter(Department.Code == department)
        .one_or_none()
    )
    if res is None:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        return DepartmentReport.from_orm(res)


@dept.post("/")
def add_department(
    dept: DepartmentReport, resp: Response, db: Session = Depends(get_db),
):
    res = db.query(Department).filter(Department.Code == dept.Code).one_or_none()

    if res is None:
        obj = Department(Code=dept.Code, Name=dept.Name)
        db.add(obj)
    db.commit()


@dept.put("/")
def update_department(
    dept: DepartmentReport, resp: Response, db: Session = Depends(get_db)
):
    res: Union[Department, None] = db.query(Department).filter(
        Department.Code == dept.Code
    ).one_or_none()

    if res is None:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        res.Name = dept.Name

    db.commit()
