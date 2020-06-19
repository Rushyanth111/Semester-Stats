from fastapi import APIRouter
from pydantic import BaseModel


student_central = APIRouter()


class ListRequest(BaseModel):
    Batch: int
    Semester: int
    Department: str


@student_central.post("/list")
def get_student_list(req: ListRequest):
    return None
