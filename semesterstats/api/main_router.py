from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware


from .Student import student_central
from .Department import department
from .Subject import subject
from .Batch import batch
from .FileUpload import upload_route

App = FastAPI()
App.add_middleware(GZipMiddleware)
App.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

App.include_router(department, prefix="/dept")
App.include_router(student_central, prefix="/student")
App.include_router(subject, prefix="/subject")
App.include_router(batch, prefix="/batch")
App.include_router(upload_route, prefix="/file")
