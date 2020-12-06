from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from ..crud.student import (
    get_student,
    get_student_backlogs,
    get_student_scores,
    get_student_subject,
    is_student_exists,
    put_student,
    update_student,
    get_student_summary,
)
from ..crud.subject import is_subject_exist
from ..database import get_db
from ..reciepts import ScoreReciept, StudentReciept
from ..reports import StudentReport
from .exceptions import (
    StudentConflictException,
    StudentDoesNotExist,
    SubjectDoesNotExist,
)

student = APIRouter()


def common_student_verify(usn: str, db: Session = Depends(get_db)) -> str:
    if not is_student_exists(db, usn):
        raise StudentDoesNotExist
    return usn


@student.get("/{usn}", response_model=StudentReciept, status_code=status.HTTP_200_OK)
def student_get(
    usn: str = Depends(common_student_verify), db: Session = Depends(get_db)
):
    return get_student(db, usn)


@student.get(
    "/{usn}/scores", response_model=List[ScoreReciept], status_code=status.HTTP_200_OK
)
def student_get_scores(
    sem: int = None,
    usn: str = Depends(common_student_verify),
    db: Session = Depends(get_db),
):
    res = get_student_scores(db, usn, sem)
    ret = [ScoreReciept.from_orm(x) for x in res]
    return ret


@student.get("/{usn}/backlogs", response_model=List[ScoreReciept])
def student_get_backlog(
    sem: int = None,
    usn: str = Depends(common_student_verify),
    db: Session = Depends(get_db),
):
    res = get_student_backlogs(db, usn, sem)
    ret = [ScoreReciept.from_orm(x) for x in res]
    return ret


@student.get("/{usn}/subject/{subcode}", response_model=ScoreReciept)
def student_get_subject_score(
    subcode: str,
    usn: str = Depends(common_student_verify),
    db: Session = Depends(get_db),
):
    if not is_subject_exist(db, subcode):
        raise SubjectDoesNotExist
    return get_student_subject(db, usn, subcode)


@student.post("/", status_code=status.HTTP_201_CREATED)
def student_insert(obj: StudentReport, db: Session = Depends(get_db)):
    try:
        put_student(db, obj)
    except IntegrityError:
        raise StudentConflictException(obj.Usn)


@student.put("/{usn}", status_code=status.HTTP_201_CREATED)
def student_update(
    obj: StudentReport,
    usn: str = Depends(common_student_verify),
    db: Session = Depends(get_db),
):
    try:
        update_student(db, usn, obj)
    except IntegrityError:
        raise StudentConflictException(obj.Usn)


@student.get("/{usn}/summary", status_code=status.HTTP_200_OK)
def student_summary(
    usn: str = Depends(common_student_verify), db: Session = Depends(get_db)
):
    ret = get_student_summary(db, usn)

    return ret
