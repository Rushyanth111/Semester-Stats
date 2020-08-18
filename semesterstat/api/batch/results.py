from fastapi import APIRouter
from ..common.reports import ScoreReport

results = APIRouter()


@results.get("/{department}/{batch}/{semester}", response_model=ScoreReport)
async def get_batch_results(department: str, batch: int, semester: int):
    pass
