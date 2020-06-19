from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware


from .Student import student_central

App = FastAPI()
App.add_middleware(GZipMiddleware)

App.include_router(student_central, prefix="/{department}")
