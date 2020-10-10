from fastapi import APIRouter, Depends, status
from sqlalchemy.exc import IntegrityError

from ..crud.subject import get_subject, is_subject_exist, put_subject, update_subject
from ..database import get_db
from ..generator import convert_subject
from ..reciepts import SubjectReciept
from ..reports import SubjectReport
from .exceptions import SubjectConflictException, SubjectDoesNotExist

subject = APIRouter()


def common_subcode_verify(subcode: str, db=Depends(get_db)) -> str:
    if not is_subject_exist(db, subcode):
        raise SubjectDoesNotExist
    return subcode


@subject.get("/{subcode}", response_model=SubjectReciept)
def subject_get(subcode: str = Depends(common_subcode_verify), db=Depends(get_db)):
    return convert_subject(get_subject(db, subcode))


@subject.post("/", status_code=status.HTTP_201_CREATED)
def subject_insert(obj: SubjectReport, db=Depends(get_db)):
    try:
        put_subject(db, obj)
    except IntegrityError:
        raise SubjectConflictException(obj.Code)


@subject.put("/{subcode}", status_code=status.HTTP_201_CREATED)
def subject_update(
    obj: SubjectReport,
    subcode: str = Depends(common_subcode_verify),
    db=Depends(get_db),
):
    try:
        update_subject(db, subcode, obj)
    except IntegrityError:
        raise SubjectConflictException(obj.Code)
