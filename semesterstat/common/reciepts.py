from pydantic import BaseModel
from typing import List, Optional


class RecieptBaseModel(BaseModel):
    class Config:
        orm_mode = True


class DepartmentReciept(RecieptBaseModel):
    Code: str
    Name: str

    class Config:
        schema_extra = {
            "example": {
                "Code": "XE",
                "Name": "The Department Name That is Having the Code XE",
            }
        }


class ScoreReciept(RecieptBaseModel):
    Usn: str
    SubjectCode: str
    Internals: int
    Externals: int

    class Config:
        schema_extra = {
            "example": {
                "Usn": "1CR16CS001",
                "SubjectCode": "15CS71",
                "Internals": 40,
                "Externals": 60,
            }
        }


class ScoreMinimalReciept(RecieptBaseModel):
    SubjectCode: str
    Internals: int
    Externals: int

    class Config:
        schema_extra = {
            "example": {"SubjectCode": "15CS71", "Internals": 40, "Externals": 60}
        }


class StudentReciept(RecieptBaseModel):
    Usn: str
    Name: str
    Batch: int
    Department: str

    class Config:
        schema_extra = {
            "example": {
                "Usn": "1CR16CS001",
                "Name": "Roy Harris",
                "Batch": 2016,
                "Department": "CS",
            }
        }


class UsnStudentReciept(RecieptBaseModel):
    Usn: str

    class Config:
        schema_extra = {"example": {"Usn": "1CR16CS001"}}


class StudentScoreReciept(RecieptBaseModel):
    Usn: str
    Name: str
    Batch: int
    Department: str
    Scores: List[ScoreMinimalReciept]

    class Config:
        schema_extra = {
            "example": {
                "Usn": "1CR16CS001",
                "Name": "Roy Harris",
                "Batch": 2016,
                "Department": "CS",
                "Scores": [
                    {"SubjectCode": "15CS71", "Internals": 40, "Externals": 60},
                    {"SubjectCode": "15CS72", "Internals": 40, "Externals": 60},
                ],
            }
        }


class SubjectReciept(RecieptBaseModel):
    Code: str
    Name: str
    Semester: int
    Scheme: int
    Department: str
    MinExt: Optional[int]
    MinTotal: Optional[int]
    Credits: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "Code": "17CS51",
                "Name": "Subject Name",
                "Semester": 6,
                "Scheme": 2017,
                "Department": "CS",
            }
        }
