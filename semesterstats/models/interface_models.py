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
    ScoreSemester: int
    ScoreInternals: int
    ScoreExternals: int


class BacklogScoreModel(BaseModel):
    ScoreSerialNumber: str
    ScoreSubjectCode: str
    ScoreSemester: int
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


def score_to_backlog(score_record: ScoreModel) -> BacklogScoreModel:
    d = score_record.dict()

    backlog_record = {}

    for key in d.keys():
        # Replace Score with Backlog but retain value
        backlog_record[key.replace("Score", "Backlog")] = d[key]

    return BacklogScoreModel.construct(**backlog_record)
