from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn.config import logger

from semesterstat.database.models import BatchSchemeInfo

from ..constants import batch_dict, dept_dict
from ..database import Department, session_create
from .batch import batch
from .bulk import bulk
from .dept import dept
from .student import student
from .subject import subject

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
General Documentation of my Intention:

GET : For Records that have very little Q-Params
POST : For Inserting Records. Notable Exception is Search, /search/ with Params.
PATCH: Modfies Record.
DELETE: Remove Record.
"""


@app.on_event("startup")
async def startup_event():
    db = session_create()

    if db.query(Department).count() == 0:
        logger.info("Inserting Department Details, Previously None")
        db.bulk_insert_mappings(
            Department,
            [{"Code": code, "Name": name} for code, name in dept_dict.items()],
        )

    if db.query(BatchSchemeInfo).count() == 0:
        logger.info("Inserting Batch Details, Previously None")
        db.bulk_insert_mappings(
            BatchSchemeInfo,
            [
                {"Batch": batch, "Scheme": scheme}
                for batch, scheme in batch_dict.items()
            ],
        )

    db.commit()
    db.close()


app.include_router(batch, prefix="/batch", tags=["Batch"])
app.include_router(dept, prefix="/dept", tags=["Department"])
app.include_router(student, prefix="/student", tags=["Student"])
app.include_router(subject, prefix="/subject", tags=["Subject"])
app.include_router(bulk, prefix="/bulk", tags=["Private API"])
