# https://pydantic-docs.helpmanual.io/usage/validators/#validate-always
from pydantic import BaseModel, validator
from typing import List, Optional
from ...common.extractor import (
    batch_from_usn,
    dept_from_usn,
    semester_from_subject,
    scheme_from_subject,
    dept_from_subject,
)


class StudentReport(BaseModel):
    Usn: str
    Name: str
    Batch: Optional[int]
    Department: Optional[str]

    @validator("Batch", pre=True, always=True)
    def set_batch(cls, v, values):
        return batch_from_usn(values["Usn"])

    @validator("Department", pre=True, always=True)
    def set_dept(cls, v, values):
        return dept_from_usn(values["Usn"])


class SubjectReport(BaseModel):
    Code: str
    Name: str
    Semester: Optional[int]
    Scheme: Optional[int]
    Department: Optional[str]

    @validator("Semester", pre=True, always=True)
    def set_semester(cls, v, values):
        return semester_from_subject(values["Code"])

    @validator("Scheme", pre=True, always=True)
    def set_scheme(cls, v, values):
        return scheme_from_subject(values["Code"])

    @validator("Department", pre=True, always=True)
    def set_dept(cls, v, values):
        return dept_from_subject(values["Code"])


class ScoreReport(BaseModel):
    Usn: str
    SubjectCode: str
    Internals: int
    Externals: int


class Report(BaseModel):
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


class BulkReport(BaseModel):
    report: List[Report]
