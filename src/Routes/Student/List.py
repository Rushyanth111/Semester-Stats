from fastapi import APIRouter
from pydantic import BaseModel

StudentList = APIRouter()




class Response(BaseModel):
    Name: str
    Some: str


@StudentList.get("/list", response_model=Response)
def getStudentList():
    return {
        "Name":"Something",
        "Some":"SomethingElseI"
    }
