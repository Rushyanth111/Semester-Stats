from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from ...response_builder import getList


student_central = APIRouter()


class ListRequest(BaseModel):
    Batch: int
    Semester: int
    Department: str


class Mark(BaseModel):
    Code: str
    Internal: int
    External: int
    Total: int
    Result: str
    Class: str


class Overall(BaseModel):
    Total: int
    Result: str


class Student(BaseModel):
    Name: str
    USN: str
    Section: str
    Marks: List[Mark]
    Overall: Overall


@student_central.post("/list", response_model=List[Student])
def get_student_list(Req: ListRequest):
    result = getList(Req.Batch, Req.Semester, Req.Department)
    return result
