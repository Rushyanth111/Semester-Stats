from fastapi import APIRouter


subject = APIRouter()


@subject.get("/{subcode}")
def get_subject():
    pass


@subject.post("/")
def add_subject():
    pass


@subject.put("/")
def update_subject():
    pass
