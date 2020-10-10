from fastapi import APIRouter, status
from fastapi.params import Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from semesterstat.crud.dept import get_all_dept

from ..crud.dept import (
    get_dept_by_code,
    is_dept_exist,
    put_department,
    update_department,
)
from ..database.database import get_db
from ..reciepts import DepartmentReciept
from ..reports import DepartmentReport
from .exceptions import DeptConflictException, DeptDoesNotExist

dept = APIRouter()


def common_department_verify(dept: str, db: Session = Depends(get_db)) -> str:
    if not is_dept_exist(db, dept):
        raise DeptDoesNotExist
    return dept


@dept.get(
    "/",
    responses={
        200: {
            "content": {
                "application/json": {
                    "example": ["CS", "TE", "MBA", "TE"],
                    "schema": {
                        "title": "DeptListReciept",
                        "type": "array",
                        "items": {"type": "string"},
                    },
                }
            }
        }
    },
)
def dept_get_all(db: Session = Depends(get_db)):
    return get_all_dept(db)


@dept.get("/{dept}", response_model=DepartmentReciept)
def department_get(
    dept: str = Depends(common_department_verify), db: Session = Depends(get_db)
):
    return get_dept_by_code(db, dept)


@dept.post("/", status_code=status.HTTP_204_NO_CONTENT)
def department_add(obj: DepartmentReport, db: Session = Depends(get_db)):
    try:
        put_department(db, obj)
    except IntegrityError:
        raise DeptConflictException(obj.Code)


@dept.put("/{dept}", status_code=status.HTTP_204_NO_CONTENT)
def department_update(
    dept: str = Depends(common_department_verify),
    obj: DepartmentReport = None,
    db: Session = Depends(get_db),
):
    try:
        update_department(db, dept, obj)
    except IntegrityError:
        raise DeptConflictException(obj.Code)
