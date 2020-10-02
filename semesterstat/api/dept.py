from typing import List

from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from semesterstat.crud.dept import get_all_dept

from ..common.generator import convert_dept
from ..common.reciepts import DepartmentReciept
from ..common.reports import DepartmentReport
from ..crud.dept import (
    get_dept_by_code,
    is_dept_exist,
    put_department,
    update_department,
)
from ..database import get_db

dept = APIRouter()


def common_department_verify(dept: str, db: Session = Depends(get_db)) -> str:
    if not is_dept_exist(db, dept):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="No Such Department"
        )
    return dept


@dept.get("/", response_model=List[str])
def dept_get_all(db: Session = Depends(get_db)):
    return get_all_dept(db)


@dept.get("/{dept}", response_model=DepartmentReciept)
def department_get(
    dept: str = Depends(common_department_verify), db: Session = Depends(get_db)
):
    return convert_dept(get_dept_by_code(db, dept))


@dept.post("/")
def department_add(
    dept: DepartmentReport, db: Session = Depends(get_db),
):
    put_department(db, dept)


@dept.put("/{dept}")
def department_update(
    dept: str = Depends(common_department_verify),
    obj: DepartmentReport = None,
    db: Session = Depends(get_db),
):
    update_department(db, dept, obj)
