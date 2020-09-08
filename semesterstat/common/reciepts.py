from pydantic import BaseModel
from typing import List


class RecieptBaseModel(BaseModel):
    class Config:
        orm_mode = True


class DepartmentReciept(RecieptBaseModel):
    Code: str
    Name: str


class ScoreReciept(RecieptBaseModel):
    Usn: str
    SubjectCode: str
    Internals: int
    Externals: int


class ScoreMinimalReciept(RecieptBaseModel):
    SubjectCode: str
    Internals: int
    Externals: int


class StudentReciept(RecieptBaseModel):
    Usn: str
    Name: str
    Batch: int
    Department: str


class UsnStudentReciept(RecieptBaseModel):
    Usn: str


class ListUsnStudentReciept(RecieptBaseModel):
    UsnList: List[UsnStudentReciept]


class StudentScoreReciept(RecieptBaseModel):
    Usn: str
    Name: str
    Batch: int
    Department: str
    Scores: List[ScoreMinimalReciept]


class SubjectReciept(RecieptBaseModel):
    Code: str
    Name: str
    Semester: int
    Scheme: int
    Department: str
