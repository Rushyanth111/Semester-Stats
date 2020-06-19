from fastapi import APIRouter
from ...config import db

student_central = APIRouter()


@student_central.get("/{student}/summary")
def get_summary(batch: int, semester: int, department: str):
    return {"error": "method not available"}


@student_central.get("/{student}/backlogs")
def get_student_backlogs(student: str):
    return db.get_backlogs(usn=student)


@student_central.get("/{student}/{semester}")
def get_student_semester(student: str, semester: int):
    return db.get_student_semester_scores(student, semester)
