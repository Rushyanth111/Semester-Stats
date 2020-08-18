from .results import results
from .upload import upload
from fastapi import APIRouter

batch = APIRouter()

batch.include_router(results, prefix="/result")
batch.include_router(upload)
