# These Define the Inserting Interfaces used;

# The rationale behind these interfaces is that any single parser later
# on can be used.
from typing import List
from .basic_models import Department
from .insert_interface_models import DepartmentModel
from peewee import SqliteDatabase


class InsertInterface:
    db: SqliteDatabase

    def __init__(self):
        pass

    def insert_department(self, department: DepartmentModel) -> bool:
        record, created = Department.get_or_create(
            DepartmentCode=department.DepartmentCode,
            DepartmentName=department.DepartmentName,
        )
        return created

    def insert_department_bulk(self, department_list: List[DepartmentModel]) -> int:
        department_tuples = []
        for x in department_list:
            department_tuples.append(x.__dict__)

        with self.db.atomic():
            lines_changed = Department.insert_many(department_tuples)
        return lines_changed

    def insert_student(self, student_record):
        pass

    def insert_score(self, score_record):
        pass

    def insert_teacher(self, teacher_record):
        pass

    def insert_student_bulk(self):
        pass

    def insert_score_bulk(self):
        pass

    def insert_teacher_bulk(self):
        pass
