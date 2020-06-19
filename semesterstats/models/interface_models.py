from pydantic import BaseModel


class DepartmentModel(BaseModel):
    DepartmentCode: str
    DepartmentName: str


class StudentModel(BaseModel):
    StudentUSN: str
    StudentName: str
    StudentBatch: int
    StudentDepartment: str


class ScoreModel(BaseModel):
    ScoreSerialNumber: str
    ScoreSubjectCode: str
    ScoreYear: int
    ScoreYearIndicator: bool
    ScoreInternals: int
    ScoreExternals: int


class BacklogScoreModel(BaseModel):
    ScoreSerialNumber: str
    ScoreSubjectCode: str
    ScoreYear: int
    ScoreYearIndicator: bool
    ScoreInternals: int
    ScoreExternals: int


class SubjectModel(BaseModel):
    SubjectCode: str
    SubjectName: str
    SubjectSemester: int
    SubjectScheme: str
    SubjectDepartment: str


class TeacherModel(BaseModel):
    TeacherUSN: str
    TeacherName: str


class TeacherTaughtModel(BaseModel):
    TeacherUSN: str
    TeacherBatch: int
