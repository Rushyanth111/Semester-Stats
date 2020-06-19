from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware


from .Student import student_central
from .Department import department

App = FastAPI()
App.add_middleware(GZipMiddleware)

App.include_router(student_central, prefix="/{department}")
App.include_router(department, prefix="/{department}")
