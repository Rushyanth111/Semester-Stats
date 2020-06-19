# This interface was designed as a single stop solution to retrieve everything from
from peewee import SqliteDatabase
from .basic_models import Department, BatchSchemeInfo, Student, Subject, Score
from playhouse.shortcuts import model_to_dict


class GetInterface:
    db: SqliteDatabase

    def __init__(self):
        pass

    def get_departement(self, department_code: str):
        return Department.get_or_none(DepartmentCode=department_code)

    def get_backlog(self):
        pass

    def get_backlogs(self):
        pass

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
                & (Subject.SubjectDepartment == department)
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
                (Score.ScoreYear == year)
                & (Score.ScoreYearIndicator == year_ind)
                & (Score.ScoreSerialNumber.in_(usns))
                & (Score.ScoreSubjectCode.in_(subject_codes))
            )
        ]
