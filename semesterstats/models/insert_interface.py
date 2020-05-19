# These Define the Inserting Interfaces used;

# The rationale behind these interfaces is that any single parser later
# on can be used.
from typing import List
from .basic_models import DepartmentDetails
from .insert_interface_models import DepartmentStructure


class InsertInterface:
    def __init__(self, batch: int, scheme: int):
        """Insert Interface is an Interface to Insert data
        for a given Batch.

        Arguments:
            batch {int} -- The Batch to be processed on
            scheme {int} -- The Scheme to be processed on
        """
        self.batch = batch
        self.scheme = scheme

    def insert_department(self, department: DepartmentStructure) -> bool:
        record, created = DepartmentDetails.get_or_create(
            DepartmentCode=department.Code, DepartmentName=department.Name
        )
        return created

    def insert_student(self, student_record):
        pass

    def insert_score(self, score_record):
        pass

    def insert_teacher(self, teacher_record):
        pass

    def insert_department_bulk(self):
        pass

    def insert_student_bulk(self):
        pass

    def insert_score_bulk(self):
        pass

    def insert_teacher_bulk(self):
        pass
