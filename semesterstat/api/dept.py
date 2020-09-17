from fastapi import APIRouter, HTTPException, Response, status
from fastapi.params import Depends
from sqlalchemy.orm.session import Session

from ..common import DepartmentReport, DepartmentReciept, convert_dept
from ..crud import get_dept_by_code, is_dept_exist, put_department, update_department
from ..database import get_db

dept = APIRouter()


def common_department_verify(dept: str, db: Session = Depends(get_db)) -> str:
    if not is_dept_exist(db, dept):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="No Such Department"
        )
    return dept


@dept.get("/{dept}", response_model=DepartmentReciept)
def department_get(
    dept: str = Depends(common_department_verify), db: Session = Depends(get_db)
):
    return convert_dept(get_dept_by_code(db, dept))


@dept.post("/")
def department_add(
    dept: DepartmentReport, resp: Response, db: Session = Depends(get_db),
):
    put_department(db, dept)


@dept.put("/{dept}")
def department_update(
    dept: str = Depends(common_department_verify),
    obj: DepartmentReport = None,
    db: Session = Depends(get_db),
):
    update_department(db, dept, obj)
