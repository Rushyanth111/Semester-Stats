# These Define the Inserting Interfaces used;

# The rationale behind these interfaces is that any single parser later
# on can be used.
from typing import List
from .basic_models import DepartmentDetails
from .insert_interface_models import DepartmentStructure
from peewee import SqliteDatabase


class InsertInterface:
    db: SqliteDatabase

    def __init__(self):
        pass

    def insert_department(self, department: DepartmentStructure) -> bool:
        record, created = DepartmentDetails.get_or_create(
            DepartmentCode=department.Code, DepartmentName=department.Name
        )
        return created

    def insert_department_bulk(self, department_list: List[DepartmentStructure]) -> int:
        department_tuples = []
        for x in department_list:
            department_tuples.append((x.Code, x.Name))

        with self.db.atomic():
            lines_changed = DepartmentDetails.insert_many(
                department_tuples,
                [DepartmentDetails.DepartmentCode, DepartmentDetails.DepartmentName],
            )
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
