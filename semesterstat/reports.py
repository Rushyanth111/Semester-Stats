from typing import List, Optional

from pydantic import BaseModel, validator

from .common.subject_extractor import (
    get_subject_dept,
    get_subject_scheme,
    get_subject_semester,
)
from .common.usn_extractor import get_usn_batch, get_usn_dept

# https://pydantic-docs.helpmanual.io/usage/validators/#validate-always

# List Optional[] Validation if Needed:
# https://github.com/samuelcolvin/pydantic/issues/367


class ReportBaseModel(BaseModel):
    class Config:
        orm_mode = True


class DepartmentReport(ReportBaseModel):
    Code: str
    Name: str

    def __eq__(self, o: "DepartmentReport") -> bool:
        return self.Code == o.Code

    def __hash__(self) -> int:
        return hash(self.Code)


class StudentReport(ReportBaseModel):
    Usn: str
    Name: str
    Batch: Optional[int]
    Department: Optional[str]

    Scores: Optional[List["ScoreReport"]]

    @validator("Batch", pre=True, always=True)
    def set_batch(cls, v, values):
        if "Usn" in values:
            return get_usn_batch(values["Usn"])
        else:
            return None

    @validator("Department", pre=True, always=True)
    def set_dept(cls, v, values):
        if "Usn" in values:
            return get_usn_dept(values["Usn"])
        else:
            return None

    def __hash__(self) -> int:
        return hash(self.Usn)

    def __eq__(self, o: "StudentReport") -> bool:
        return self.Usn == o.Usn


class SubjectReport(ReportBaseModel):
    Code: str
    Name: str
    Semester: Optional[int]
    Scheme: Optional[int]
    Department: Optional[str]
    MinExt: Optional[int]
    MinTotal: Optional[int]
    MaxTotal: Optional[int]
    Credits: Optional[int]

    @validator("Semester", pre=True, always=True)
    def set_semester(cls, v, values):
        if "Code" in values:
            return get_subject_semester(values["Code"])
        else:
            return None

    @validator("Scheme", pre=True, always=True)
    def set_scheme(cls, v, values):
        if "Code" in values:
            return get_subject_scheme(values["Code"])
        else:
            return None

    @validator("Department", pre=True, always=True)
    def set_department(cls, v, values):
        if "Code" in values:
            return get_subject_dept(values["Code"])
        else:
            return None

    def __hash__(self) -> int:
        return hash(self.Code)

    def __eq__(self, o: "SubjectReport") -> bool:
        return self.Code == o.Code


class ScoreReport(ReportBaseModel):
    Usn: str
    SubjectCode: str
    Internals: int
    Externals: int

    def __hash__(self) -> int:
        return hash((self.Usn, self.SubjectCode))

    def __eq__(self, o: "ScoreReport") -> bool:
        return self.Usn == o.Usn and self.SubjectCode == o.SubjectCode

    def __gt__(self, o: "ScoreReport") -> bool:
        return (self.Internals + self.Externals) > (o.Internals + o.Externals)

    def __ge__(self, o: "ScoreReport") -> bool:
        return (self.Internals + self.Externals) >= (o.Internals + o.Externals)


DepartmentReport.update_forward_refs()
StudentReport.update_forward_refs()
