from fastapi import APIRouter
from ...config import db

department = APIRouter()


@department.get("/detail")
def department_details(department: str):
    return db.get_departement(department)
