from fastapi import APIRouter

results = APIRouter()


@results.get("/{department}/{batch}/{semester}")
async def get_batch_results(department: str, batch: str, semester: int):
    return {"Hi": "Hello World!"}
