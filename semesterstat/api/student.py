from fastapi import APIRouter

student = APIRouter()


@student.get("/{Usn}")
def get_student():
    pass


@student.post("/")
def insert_student():
    pass


@student.put("/")
def update_student():
    pass


@student.get("/{Usn}/summary")
def get_student_summary():
    pass


@student.get("/{Usn}/detail")
def get_student_detail():
    pass
