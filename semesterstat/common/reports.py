from typing import List, Optional

from pydantic import BaseModel, validator

from .subject_extractor import (
    get_subject_dept,
    get_subject_scheme,
    get_subject_semester,
)
from .usn_extractor import get_usn_batch, get_usn_dept

# https://pydantic-docs.helpmanual.io/usage/validators/#validate-always

# List Optional[] Validation if Needed:
# https://github.com/samuelcolvin/pydantic/issues/367


class ReportBaseModel(BaseModel):
    class Config:
        orm_mode = True


class DepartmentReport(ReportBaseModel):
    Code: str
    Name: str

    Subjects: Optional[List["SubjectReport"]]
    Students: Optional[List["StudentReport"]]


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


class SubjectReport(ReportBaseModel):
    Code: str
    Name: str
    Semester: Optional[int]
    Scheme: Optional[int]
    Department: Optional[str]

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


class ScoreReport(ReportBaseModel):
    Usn: str
    SubjectCode: str
    Internals: int
    Externals: int

    def __hash__(self) -> int:
        return hash(self.Usn + self.SubjectCode)


class Report(ReportBaseModel):
    Usn: str
    Name: str
    Subcode: str
    Subname: str
    Internals: int
    Externals: int

    def export_student(self) -> StudentReport:
        return StudentReport(Usn=self.Usn, Name=self.Name)

    def export_score(self) -> ScoreReport:
        return ScoreReport(
            Usn=self.Usn,
            SubjectCode=self.Subcode,
            Internals=self.Internals,
            Externals=self.Externals,
        )

    def export_subject(self) -> SubjectReport:
        return SubjectReport(Code=self.Subcode, Name=self.Subname)


DepartmentReport.update_forward_refs()
StudentReport.update_forward_refs()
