from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from uvicorn.config import logger

from ..common import Report
from ..database import Score, Student, Subject, get_db

bulk = APIRouter()

"""
The Bulk API Router handles the Bulk Transactions of the User, namely Updating Reports
and Adding new Reports.

"""


@bulk.post("/", status_code=status.HTTP_204_NO_CONTENT)
async def update_batch_results(reports: List[Report], db: Session = Depends(get_db)):
    student_list = []
    student_list_update = []
    sub_list = []
    sub_list_update = []
    score_list = []
    score_list_update = []
    # Split Each of the Report into the 4 main Categories.
    for rp in reports:
        x = rp.export_student()
        if db.query(Student).filter(Student.Usn == x.Usn).one_or_none() is not None:
            student_list.append(x.dict())
        else:
            student_list_update.append(x.dict())

        x = rp.export_subject()
        if db.query(Subject).filter(Subject.Code == x.Code).one_or_none() is not None:
            sub_list.append(x.dict())
        else:
            sub_list_update.append(x.dict())

        x = rp.export_score()
        if (
            db.query(Score)
            .filter(Score.SubjectCode == x.SubjectCode, Score.Usn == x.Usn)
            .one_or_none()
            is not None
        ):
            score_list.append(x.dict())
        else:
            score_list_update.append(x.dict())

    # Add them into the database
    # In the Order of:
    # Dept, Subject, Student, Score
    logger.info("Updating batch_results")

    db.bulk_insert_mappings(Student, student_list)
    db.bulk_insert_mappings(Subject, sub_list)
    db.bulk_insert_mappings(Score, score_list)

    db.bulk_update_mappings(Student, student_list_update)
    db.bulk_update_mappings(Subject, sub_list_update)
    db.bulk_update_mappings(Score, score_list_update)

    db.commit()
