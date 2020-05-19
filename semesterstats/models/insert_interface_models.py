from pydantic import BaseModel
from typing import List


class DepartmentStructure(BaseModel):
    Code: str
    Name: str


class StudentStructure(BaseModel):
    SerialNumber: str
    Name: str
    Department: str


class ScoreStructure(BaseModel):
    SerialNumber: str
    SubjectCode: str
    SubjectSemester: str
    Arrear: bool
    Internals: int
    Externals: int


class SubjectStructure(BaseModel):
    Code: str
    Name: str


class TeacherStructure(BaseModel):
    USN: str
    Name: str


class TeacherDetailsStructure(BaseModel):
    USN: str
    Batch: List[int]
