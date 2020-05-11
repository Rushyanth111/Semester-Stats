from fastapi import FastAPI
from .Student import StudentCentral

App = FastAPI()

App.include_router(StudentCentral, prefix="/student")
