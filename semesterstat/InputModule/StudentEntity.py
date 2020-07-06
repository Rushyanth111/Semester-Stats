from pydantic import BaseModel
from typing import List


class StudentEntity(BaseModel):
    usn: str
    name: str
    batch: int
    department: str

    @staticmethod
    def create(usn: str, name: int, batch: int, department: str) -> "StudentEntity":
        return StudentEntity(usn=usn, name=name, batch=batch, department=department)

    @staticmethod
    def submit(objects: List["StudentEntity"]):
        pass
