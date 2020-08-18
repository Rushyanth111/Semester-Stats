from typing import List

from fastapi import APIRouter
from fastapi.logger import logger
from fastapi.params import Depends
from sqlalchemy.orm.session import Session

from ...database import Score, Student, Subject, get_db
from ..common.reports import Report

insert = APIRouter()


@insert.post("/insert", status_code=201)
async def parse_batch_results(reports: List[Report], db: Session = Depends(get_db)):
    student_list = []
    sub_list = []
    score_list = []
    # Split Each of the Report into the 4 main Categories.
    for rp in reports:
        x = rp.export_student()
        if db.query(Student).filter(Student.Usn == x.Usn).one_or_none() is None:
            student_list.append(x.dict())

        x = rp.export_subject()
        if db.query(Subject).filter(Subject.Code == x.Code).one_or_none() is None:
            sub_list.append(x.dict())

        x = rp.export_score()
        if (
            db.query(Score)
            .filter(Score.SubjectCode == x.SubjectCode, Score.Usn == x.Usn)
            .one_or_none()
            is None
        ):
            score_list.append(x.dict())

    # Add them into the database
    # In the Order of:
    # Dept, Subject, Student, Score
    logger.info("Parsing batch_results")

    db.bulk_insert_mappings(Student, student_list)
    db.bulk_insert_mappings(Subject, sub_list)
    db.bulk_insert_mappings(Score, score_list)

    db.commit()
