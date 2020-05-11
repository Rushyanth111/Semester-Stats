from fastapi import APIRouter
from pydantic import BaseModel, parse_obj_as
from typing import List
from ...databaseFunctions import getList

StudentList = APIRouter()


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


@StudentList.post("/list", response_model=List[Student])
def getStudentList(req: ListRequest):
    result = getList(req.Batch, req.Semester, req.Department)
    return result
