from typing import Counter, Dict, List, Optional

from pydantic import BaseModel


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

    def __hash__(self) -> int:
        return hash((self.Code))

    def __eq__(self, o: "DepartmentReciept") -> bool:
        return self.Usn


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

    def __hash__(self) -> int:
        return hash((self.Usn, self.SubjectCode))

    def __eq__(self, o: "ScoreReciept") -> bool:
        return self.Usn == o.Usn and self.SubjectCode == o.SubjectCode


class ScoreMinimalReciept(RecieptBaseModel):
    SubjectCode: str
    Internals: int
    Externals: int

    class Config:
        schema_extra = {
            "example": {"SubjectCode": "15CS71", "Internals": 40, "Externals": 60}
        }

    def __hash__(self) -> int:
        return hash(self.SubjectCode)

    def __eq__(self, o: "ScoreMinimalReciept") -> bool:
        return self.SubjectCode == o.SubjectCode


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

    def __hash__(self) -> int:
        return hash(self.Usn)

    def __eq__(self, o: "StudentReciept") -> bool:
        return self.Usn == o.Usn


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

    def __hash__(self) -> int:
        return hash((self.Usn, tuple(sorted(self.Scores, key=lambda x: x.SubjectCode))))

    def __eq__(self, o: "StudentScoreReciept") -> bool:
        return self.Usn == o.Usn and Counter(self.Scores) == Counter(o.Scores)


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

    def __hash__(self) -> int:
        return hash(self.Code)

    def __eq__(self, o: "SubjectReciept") -> bool:
        return self.Code == o.Code


class SubjectSummaryReciept(RecieptBaseModel):
    Appeared: int
    Failed: int
    Fcd: int
    Fc: int
    Sc: int
    PassPercent: float
    Pass: int


class SummaryReciept(RecieptBaseModel):
    Appeared: int
    Fcd: int
    Fc: int
    Sc: int
    Pass: int
    Fail: int
    PassPercent: float
    Subjects: Optional[Dict[str, SubjectSummaryReciept]]
