from fastapi import FastAPI
from uvicorn.config import logger

from ..constants import dept_dict
from ..database import Department, session_create
from .batch import batch
from .dept import dept
from .student import student
from .subject import subject

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
app.include_router(student, prefix="/student")
app.include_router(subject, prefix="/subject")
