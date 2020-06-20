from typing import List
from .basic_models import Department, Student, Subject, Score, BatchSchemeInfo, Backlog
from .interface_models import (
    DepartmentModel,
    StudentModel,
    SubjectModel,
    ScoreModel,
    score_to_backlog,
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
        Department.insert(department.dict()).on_conflict_ignore().execute()

    def insert_department_bulk(self, department_list: List[DepartmentModel]) -> int:
        dept_dicts = [x.dict() for x in department_list]

        with self.db.atomic():
            lines_changed = (
                Department.insert_many(dept_dicts).on_conflict_ignore().execute()
            )
        return lines_changed

    def insert_student(self, student_record: StudentModel):
        return Student.insert(student_record.dict()).on_conflict_ignore().execute()

    def insert_student_bulk(self, student_records: List[StudentModel]):
        student_dicts = [x.dict() for x in student_records]

        with self.db.atomic():
            lines_changed = (
                Student.insert_many(student_dicts).on_conflict_ignore().execute()
            )
        return lines_changed

    def insert_score(self, score_record: ScoreModel):
        return Score.insert(score_record.dict()).on_conflict_ignore().execute()

    def insert_score_bulk(self, score_records: List[ScoreModel]):
        # Here we need to check for conflicts.
        backlog_records = []
        new_records = []

        for record in score_records:
            found = Score.select().where(
                (Score.ScoreSerialNumber == record.ScoreSerialNumber)
                & (Score.ScoreSubjectCode == record.ScoreSubjectCode)
            )
            if found.count() > 0:
                # A Backlog Score is found:
                # 1. Check for when the semester is lower: if true, then add new_record
                #    into backlog
                # 2. If same semester, check for marks, if > then add to new_record
                # 3. If the semester is higher then shunt old_record into backlog
                # 4. If Neither of Those things, add to Backlog
                if found[0].ScoreSemester < record.ScoreSemester:
                    # Existing record goes to backlog, and new record comes inplace.
                    backlog_records.append(
                        score_to_backlog(
                            ScoreModel.construct(**found.dicts()[0])
                        ).dict()
                    )
                    new_records.append(record.dict())
                elif found[0].ScoreSemester > record.ScoreSemester:
                    # If lower semester, shunt into backlog
                    backlog_records.append(score_to_backlog(record).dict())

                elif found[0].ScoreSemester == record.ScoreSemester and (
                    found[0].ScoreInternals + found[0].ScoreExternals
                ) > (record.ScoreInternals + record.ScoreExternals):
                    # If the existing Record has higher marks
                    # shunt new record into backlog
                    backlog_records.append(score_to_backlog(record).dict())
                else:
                    # If all else fails, then throw the existing record into old.
                    backlog_records.append(
                        score_to_backlog(
                            ScoreModel.construct(**found.dicts()[0])
                        ).dict()
                    )
                    new_records.append(record.dict())

            else:
                new_records.append(record.dict())

        with self.db.atomic():
            print("Inserting into Score.")
            Score.insert_many(new_records).on_conflict_replace().execute()
            Backlog.insert_many(backlog_records).execute()

        return True

    def insert_subject(self, subject_record: SubjectModel):
        return Subject.insert(subject_record.dict()).on_conflict_ignore().execute()

    def insert_subject_bulk(self, subject_records: List[SubjectModel]):
        subject_dicts = [x.dict() for x in subject_records]

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
