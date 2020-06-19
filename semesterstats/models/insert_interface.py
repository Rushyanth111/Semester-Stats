# These Define the Inserting Interfaces used;

# The rationale behind these interfaces is that any single parser later
# on can be used.
from typing import List
from .basic_models import Department, Student, Subject, Score, BatchSchemeInfo
from .interface_models import (
    DepartmentModel,
    StudentModel,
    SubjectModel,
    ScoreModel,
)
from peewee import SqliteDatabase, IntegrityError


class InsertInterface:
    db: SqliteDatabase

    def __init__(self):
        pass

    def insert_batch_scheme(self, scheme: int, batch: int):
        try:
            return BatchSchemeInfo.create(Scheme=scheme, Batch=batch)
        except IntegrityError:
            return None

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

    def insert_subject_bulk(self, subject_records: List[SubjectModel]):
        subject_dicts = [x.__dict__ for x in subject_records]

        with self.db.atomic():
            lines_changed = (
                Subject.insert_many(subject_dicts).on_conflict_ignore().execute()
            )
        return lines_changed

    def process_bulk(self):
        class StorageContainer:
            def __init__(self, model_interface_instance: InsertInterface):
                self.db = model_interface_instance
                self.dept_holder = []
                self.student_holder = []
                self.score_holder = []
                self.subject_holder = []

            def insert(self, obj):
                if isinstance(obj, DepartmentModel):
                    self.dept_holder.append(obj)
                elif isinstance(obj, StudentModel):
                    self.student_holder.append(obj)
                elif isinstance(obj, ScoreModel):
                    self.score_holder.append(obj)
                elif isinstance(obj, SubjectModel):
                    self.subject_holder.append(obj)
                else:
                    pass

            def __enter__(self):
                return self

            def __exit__(self, type, value, traceback):
                self.db.insert_department_bulk(self.dept_holder)
                self.db.insert_student_bulk(self.student_holder)
                self.db.insert_subject_bulk(self.subject_holder)
                self.db.insert_score_bulk(self.score_holder)

        return StorageContainer(self)
