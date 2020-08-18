from fastapi import FastAPI
from .batch import batch
from .department import dept

app = FastAPI()

app.include_router(batch, prefix="/batch")
app.include_router(dept, prefix="/dept")
