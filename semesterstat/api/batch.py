from typing import List, Optional

from fastapi import APIRouter, status
from fastapi.logger import logger
from fastapi.params import Depends
from sqlalchemy.orm import Session

from ..database import Score, Student, Subject, get_db
from ..common import Report, ScoreReport

batch = APIRouter()


@batch.put("/", status_code=status.HTTP_204_NO_CONTENT)
async def update_batch_results(reports: List[Report], db: Session = Depends(get_db)):
    student_list = []
    sub_list = []
    score_list = []
    # Split Each of the Report into the 4 main Categories.
    for rp in reports:
        x = rp.export_student()
        if db.query(Student).filter(Student.Usn == x.Usn).one_or_none() is not None:
            student_list.append(x.dict())

        x = rp.export_subject()
        if db.query(Subject).filter(Subject.Code == x.Code).one_or_none() is not None:
            sub_list.append(x.dict())

        x = rp.export_score()
        if (
            db.query(Score)
            .filter(Score.SubjectCode == x.SubjectCode, Score.Usn == x.Usn)
            .one_or_none()
            is not None
        ):
            score_list.append(x.dict())

    # Add them into the database
    # In the Order of:
    # Dept, Subject, Student, Score
    logger.info("Updating batch_results")

    db.bulk_update_mappings(Student, student_list)
    db.bulk_update_mappings(Subject, sub_list)
    db.bulk_update_mappings(Score, score_list)

    db.commit()


@batch.post("/", status_code=201)
async def insert_batch_results(reports: List[Report], db: Session = Depends(get_db)):
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
    logger.info("Adding batch_results")

    db.bulk_insert_mappings(Student, student_list)
    db.bulk_insert_mappings(Subject, sub_list)
    db.bulk_insert_mappings(Score, score_list)

    db.commit()


@batch.get("/{batch}/summary", response_model=ScoreReport)
async def get_batch_summary(
    batch: int, department: Optional[str] = None, semester: Optional[int] = None
):
    pass


@batch.get("/{batch}/detail")
async def get_batch_detail(
    batch: int, department: Optional[str] = None, semester: Optional[int] = None
):
    pass


@batch.get("/{batch}/list")
async def get_batch_list(
    batch: int, department: Optional[str] = None, semester: Optional[int] = None
):
    pass


@batch.get("/{batch}/backlog")
async def get_batch_backlog(
    batch: int, department: Optional[str] = None, semester: Optional[int] = None
):
    pass


@batch.get("/{batch}/detained")
async def get_batch_detained(
    batch: int, department: Optional[str] = None, semester: Optional[int] = None
):
    pass
