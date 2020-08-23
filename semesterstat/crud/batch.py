from typing import List

from sqlalchemy import or_
from sqlalchemy.orm import Session, noload
from sqlalchemy.sql.functions import func

from semesterstat.common.reports import ScoreReport, StudentReport

from ..database import Score, Student, Subject, BatchSchemeInfo


"""
Heirarchy of Batch Crud Operations:


get_batch
    |-> Department Filter   -> List Filters (Optional)
    |-> Semester Filter     -> List Filters (Optional)
    |-> Detained Filter     -> List Filters (Optional)
    |-> BackLog Filter      -> List Filters (Optional)

Purpose:
- Obtain Scores As Per the Given Parameters.

Output:
- List[Student(List[Scores])]

"""


class BatchQuery:
    def __init__(self, db: Session, batch: int) -> None:
        self.usn_batch = db.query(Student).filter(Student.Batch == batch)
        self.res = db.query(Score)

        scheme = (
            db.query(BatchSchemeInfo.Scheme)
            .filter(BatchSchemeInfo.Batch == batch)
            .scalar()
        )
        self.subject_codes = db.query(Subject).filter(Subject.Scheme == scheme)

    def dept(self, dept: str):
        self.usn_batch = self.usn_batch.filter(Student.Department == dept)

        return self

    def sem(self, sem: int):
        self.subject_codes = self.subject_codes.filter(Subject.Semester == sem)

        return self

    def backlog(self, ext_thres: int = 21, total_thres: int = 40):
        self.res = self.res.filter(
            or_(
                (Score.Internals + Score.Externals) < total_thres,
                Score.Externals < ext_thres,
            )
        )

        return self

    def detain(self, det_thres: int = 4):
        """ Having count det_thres or more """
        self.res = self.res.filter(
            Score.Usn.in_(
                self.res.group_by(Score.Usn)
                .having(func.count() > det_thres)
                .with_entities(Score.Usn)
            )
        )

        return self

    def __export(self):
        # Exporting the subqueries.
        usns = self.usn_batch.with_entities(Student.Usn)
        subcodes = self.subject_codes.with_entities(Subject.Code)

        return self.res.filter(Score.Usn.in_(usns)).filter(
            Score.SubjectCode.in_(subcodes)
        )

    def export_report(self) -> List[StudentReport]:
        scores = [ScoreReport.from_orm(x) for x in self.__export()]

        # Get the USN List, As Filtered

        students = [
            StudentReport.from_orm(x)
            for x in self.usn_batch.options(noload(Student.Scores))
        ]

        for student in students:
            for score in scores:
                if student.Usn == score.Usn:
                    student.Scores.append(score)

        return students

    def export_usns(self) -> List[str]:
        return [
            x for (x,) in self.__export().group_by(Score.Usn).with_entities(Score.Usn)
        ]
