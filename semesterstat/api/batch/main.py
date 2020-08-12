from .results import results
from fastapi import APIRouter

batch = APIRouter()

batch.include_router(results, prefix="/result")
