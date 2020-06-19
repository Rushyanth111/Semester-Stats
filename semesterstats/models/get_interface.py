# This interface was designed as a single stop solution to retrieve everything from
from peewee import SqliteDatabase
from .basic_models import Department, BatchSchemeInfo, Backlog, Student, Subject, Score
from playhouse.shortcuts import model_to_dict

from .interface_models import (
    DepartmentModel,
    ScoreModel,
    BacklogScoreModel,
    SubjectModel,
    TeacherModel,
    TeacherTaughtModel,
    StudentModel,
)


class GetInterface:
    db: SqliteDatabase

    def __init__(self):
        pass

    def get_departement(self, department_code: str) -> DepartmentModel:
        dept = list(
            Department.select()
            .where((Department.DepartmentCode == department_code))
            .objects()
        )
        if len(dept) == 0:
            return None

        return DepartmentModel.construct(**model_to_dict(dept[0]))

    def get_backlog(self):
        pass

    def get_backlogs(self, usn: str):
        return [
            BacklogScoreModel.construct(**model_to_dict(x))
            for x in Backlog.select().where((Backlog.BacklogSerialNumber == usn))
        ]

    def get_scheme(self, batch: int):
        try:
            return BatchSchemeInfo.get_or_none(Batch=batch).Scheme
        except AttributeError:  # If it is Indeed None
            return None

    def get_subject_codes(self, batch: int, semester: int, department: str):
        scheme = self.get_scheme(batch)
        return [
            x.SubjectCode
            for x in Subject.select()
            .where(
                (Subject.SubjectSemester == semester)
                & (Subject.SubjectScheme == scheme)
            )
            .execute()
        ]

    def get_subject(self, subject_code):
        r = Subject.get_or_none(SubjectCode=subject_code)
        try:
            return (
                r.SubjectCode,
                r.SubjectName,
                r.SubjectSemester,
                r.SubjectScheme,
                r.SubjectDepartment,
            )
        except AttributeError:
            return None

    def get_students_usn(self, batch: int, department: str):
        return [
            x.StudentUSN
            for x in Student.select(Student.StudentUSN)
            .where(
                (Student.StudentBatch == batch)
                & (Student.StudentDepartment == department)
            )
            .execute()
        ]

    def get_student(self, usn: int):
        return Student.get_or_none(StudentUSN=usn)

    def get_score(self, usn: int, subject_code: str):
        return model_to_dict(
            Score.get_or_none(ScoreSerialNumber=usn, ScoreSubjectCode=subject_code)
        )

    def get_scores(self, batch: int, semester: int, department: str):
        year = batch + semester // 2
        year_ind = bool(semester % 2 == 0)
        subject_codes = self.get_subject_codes(batch, semester, department)
        usns = self.get_students_usn(batch, department)
        return [
            model_to_dict(x)
            for x in Score.select().where(
                (Score.ScoreSemester == semester)
                & (Score.ScoreSerialNumber.in_(usns))
                & (Score.ScoreSubjectCode.in_(subject_codes))
            )
        ]

    def get_student_semester_scores(self, usn: str, semester: int):
        student = self.get_student(usn)
        if student is None:
            return None
        subject_codes = self.get_subject_codes(
            student.StudentBatch, semester, student.StudentDepartment
        )

        year = student.StudentBatch + semester // 2
        year_ind = bool(semester % 2 == 0)
        return [
            model_to_dict(x)
            for x in Score.select().where(
                (Score.ScoreSemester == semester)
                & (Score.ScoreSerialNumber == usn)
                & (Score.ScoreSubjectCode.in_(subject_codes))
            )
        ]
