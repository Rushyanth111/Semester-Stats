from fastapi import FastAPI
from .Student.Central import StudentCentral

App = FastAPI()

App.include_router(StudentCentral, prefix="/student")
