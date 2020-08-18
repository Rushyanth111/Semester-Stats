from .results import results
from .insert import insert
from fastapi import APIRouter

batch = APIRouter()

batch.include_router(results, prefix="/result")
batch.include_router(insert)
