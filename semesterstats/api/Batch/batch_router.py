from fastapi import APIRouter
from ...config import db


batch = APIRouter()


@batch.get("/{department}/{batch}/{semester}/detail")
def get_batch_detail(department: str, semester: int, batch: int):
    return db.get_scores(batch, semester, department)


@batch.get("/{department}/{batch}/{semester}/summary")
def get_batch_summary(department: str, semester: int, batch: int):
    return None


@batch.get("/{department}/{batch}/list")
def get_batch_students(department: str, batch: int):
    return db.get_students_usn(batch, department)
