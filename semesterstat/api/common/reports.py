from pydantic import BaseModel, validator
from typing import List, Optional
from ...common.extractor import batch_from_usn, dept_from_usn


class StudentReport(BaseModel):
    Usn: str
    Name: str
    Batch: Optional[int]
    Department: Optional[str]

    @validator("Batch", pre=True, always=True)
    def set_batch(self, v, values):
        return batch_from_usn(values["Usn"])

    @validator("Department", pre=True, always=True)
    def set_dept(self, v, values):
        return dept_from_usn(values["Usn"])


class SubjectReport(BaseModel):
    Code: str
    Name: str
    Semester: Optional[int]
    Scheme: Optional[str]
    Department: Optional[str]

    @validator("Semester", pre=True, always=True)
    def set_semester(self, v, values):
        pass

    @validator("Scheme", pre=True, always=True)
    def set_scheme(self, v, values):
        pass

    @validator("Department", pre=True, always=True)
    def set_dept(self, v, values):
        pass


class DepartmentReport(BaseModel):
    Code: str
    Name: str


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

    # https://pydantic-docs.helpmanual.io/usage/validators/#validate-always
    def export_student(self) -> StudentReport:
        return StudentReport(Usn=self.Usn, Name=self.Name)

    def export_score(self) -> ScoreReport:
        pass

    def export_department(self) -> DepartmentReport:
        pass

    def export_subject(self) -> SubjectReport:
        pass


class BulkReport(BaseModel):
    report: List[Report]
