from pydantic import BaseModel
from typing import List, Tuple

from ..Database import db, Student


class StudentEntity(BaseModel):
    usn: str
    name: str
    batch: int
    department: str

    @classmethod
    def convert_to_database_tuple(cls: "StudentEntity"):
        return (cls.usn, cls.name, cls.batch, cls.department)

    @staticmethod
    def create(usn: str, name: str, batch: int, department: str) -> "StudentEntity":
        return StudentEntity(
            usn=usn.upper(),
            name=name.upper(),
            batch=batch,
            department=department.upper(),
        )

    @staticmethod
    def submit_bulk(objects: List["StudentEntity"]):
        # Convert All of the StudentEntity Objects to Student Objects.
        stu_list: List[Tuple[str, str, int, str]] = [
            obj.convert_to_database_tuple() for obj in objects
        ]

        # Insert all of the tuples into the StudentDatabase.
        # Ignore Conflicts, do not proceed with them.

        with db.atomic():
            Student.insert_many(
                stu_list,
                fields=[Student.Usn, Student.Name, Student.Batch, Student.Department],
            ).on_conflict_ignore().execute()

    @staticmethod
    def update_student(old_id: str, stu: "StudentEntity") -> None:

        Student.update(
            Usn=stu.usn, Name=stu.name, Batch=stu.batch, department=stu.department
        ).where(Student.Usn == old_id)
