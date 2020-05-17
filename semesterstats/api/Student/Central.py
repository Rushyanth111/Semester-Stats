from fastapi import APIRouter
from .List import StudentList

StudentCentral = APIRouter()

StudentCentral.include_router(StudentList)
