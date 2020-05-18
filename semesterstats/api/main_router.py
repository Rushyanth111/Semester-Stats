from fastapi import FastAPI
from .Student import student_central

App = FastAPI()

App.include_router(student_central, prefix="/student")
