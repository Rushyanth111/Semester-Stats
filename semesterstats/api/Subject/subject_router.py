from fastapi import APIRouter
from ...config import db


subject = APIRouter()


@subject.get("/{subject_code}/detail")
def get_subject(subject_code: str):
    print(subject_code)
    return db.get_subject(subject_code)
