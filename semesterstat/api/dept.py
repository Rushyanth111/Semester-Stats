from fastapi import APIRouter, HTTPException, Response, status
from fastapi.params import Depends
from sqlalchemy.orm.session import Session

from ..common import DepartmentReport
from ..crud import get_dept_by_code, is_dept_exist, put_department, update_department
from ..database import get_db

dept = APIRouter()


def common_department_verify(dept: str, db: Session = Depends(get_db)) -> str:
    if not is_dept_exist(db, dept):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="No Such Department"
        )
    return dept


@dept.get("/{dept}")
def department_get(
    dept: str = Depends(common_department_verify), db: Session = Depends(get_db)
):
    return get_dept_by_code(db, dept)


@dept.post("/")
def department_add(
    dept: DepartmentReport, resp: Response, db: Session = Depends(get_db),
):
    put_department(db, dept)
    db.commit()


@dept.put("/{dept}")
def department_update(
    dept: str = Depends(common_department_verify),
    obj: DepartmentReport = None,
    db: Session = Depends(get_db),
):
    update_department(db, dept, obj)
