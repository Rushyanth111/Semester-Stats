from fastapi import APIRouter, Depends, HTTPException, status

from ..common import SubjectReport, SubjectReciept, convert_subject
from ..crud import (
    get_subject,
    is_subject_exist,
    put_subject,
    update_subject,
)
from ..database import get_db

subject = APIRouter()


def common_subcode_verify(subcode: str, db=Depends(get_db)) -> str:
    if not is_subject_exist(subcode):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Subject Does not Exist."
        )
    return subcode


@subject.get("/{subcode}", response_model=SubjectReciept)
def subject_get(subcode: str = Depends(common_subcode_verify), db=Depends(get_db)):
    return convert_subject(get_subject(db, subcode))


@subject.post("/")
def subject_insert(obj: SubjectReport, db=Depends(get_db)):
    put_subject(db, obj)


@subject.put("/{subcode}")
def subject_update(obj: SubjectReport, subcode: str, db=Depends(common_subcode_verify)):
    update_subject(db, subcode, obj)
