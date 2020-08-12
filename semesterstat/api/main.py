from fastapi import FastAPI
from .batch import batch

app = FastAPI()

app.include_router(batch, prefix="/batch")
