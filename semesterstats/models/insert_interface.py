# These Define the Inserting Interfaces used;

# The rationale behind these interfaces is that any single parser later
# on can be used.
from typing import List
from .basic_models import Department, Student, Subject, Score, Teacher, TeacherTaught
from .insert_interface_models import (
    DepartmentModel,
    StudentModel,
    SubjectModel,
    TeacherModel,
    ScoreModel,
    TeacherTaughtModel,
)
from peewee import SqliteDatabase


class InsertInterface:
    db: SqliteDatabase

    def __init__(self):
        pass

    def insert_department(self, department: DepartmentModel) -> bool:
        return Department.insert(department.__dict__).on_conflict_ignore().execute()

    def insert_department_bulk(self, department_list: List[DepartmentModel]) -> int:
        dept_dicts = [x.__dict__ for x in department_list]

        with self.db.atomic():
            lines_changed = (
                Department.insert_many(dept_dicts).on_conflict_ignore().execute()
            )
        return lines_changed

    def insert_student(self, student_record: StudentModel):
        return Student.insert(student_record.__dict__).on_conflict_ignore().execute()

    def insert_student_bulk(self, student_records: List[StudentModel]):
        student_dicts = [x.__dict__ for x in student_records]

        with self.db.atomic():
            lines_changed = (
                Student.insert_many(student_dicts).on_conflict_ignore().execute()
            )
        return lines_changed

    def insert_score(self, score_record: ScoreModel):
        return Score.insert(score_record.__dict__).on_conflict_ignore().execute()

    def insert_score_bulk(self, score_records: List[ScoreModel]):
        score_dicts = [x.__dict__ for x in score_records]

        with self.db.atomic():
            lines_changed = Score.replace_many(score_dicts).execute()
        return lines_changed

    def insert_subject(self, subject_record: SubjectModel):
        return Subject.insert(subject_record.__dict__).on_conflict_ignore().execute()

    def insert_subjects(self, subject_records: List[SubjectModel]):
        subject_dicts = [x.__dict__ for x in subject_records]

        with self.db.atomic():
            lines_changed = (
                Subject.insert_many(subject_dicts).on_conflict_ignore().execute()
            )
        return lines_changed

    def insert_teacher(self, teacher_record: TeacherModel):
        return Teacher.insert(teacher_record.__dict__).on_conflict_ignore().execute()

    def insert_teacher_bulk(self, teacher_records: List[TeacherModel]):
        pass
