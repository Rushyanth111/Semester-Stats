from fastapi import APIRouter
from ...config import db

student_central = APIRouter()


@student_central.post("/list")
def get_batch_results(batch: int, semester: int, department: str):
    return db.get_scores(batch, semester, department)


@student_central.get("/students")
def get_students(batch: int, department: str):
    return db.get_students_usn(batch, department)


@student_central.get("/subjects")
def get_subject_codes(batch: int, semester: int, department: str):
    return db.get_subject_codes(batch, semester, department)
