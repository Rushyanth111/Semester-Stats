from fastapi import FastAPI
from .dept import dept
from .batch import batch
from uvicorn.config import logger
from ..database import session_create, Department
from ..constants import dept_dict

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    db = session_create()

    if db.query(Department).count() == 0:
        logger.info("Inserting Department Details, Previously None")
        db.bulk_insert_mappings(
            Department,
            [{"Code": code, "Name": name} for code, name in dept_dict.items()],
        )
        db.commit()

    db.close()


app.include_router(batch, prefix="/batch")
app.include_router(dept, prefix="/dept")
