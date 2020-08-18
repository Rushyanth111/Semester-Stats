from .results import results
from .insert import insert
from .update import update
from fastapi import APIRouter

batch = APIRouter()


batch.include_router(results, prefix="/result")
batch.include_router(insert, prefix="/insert")
batch.include_router(update, prefix="/update")
