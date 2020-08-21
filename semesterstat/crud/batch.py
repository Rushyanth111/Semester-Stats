from typing import List

from sqlalchemy import func, or_
from sqlalchemy.orm import contains_eager
from sqlalchemy.orm.session import Session

from semesterstat.common.reports import StudentReport

from ..database import Score, Student, Subject


"""
Heirarchy of Batch Crud Operations:


get_batch
    |-> Department Filter   -> List Filters (Optional)
    |-> Semester Filter     -> List Filters (Optional)
    |-> Detained Filter     -> List Filters (Optional)
    |-> BackLog Filter      -> List Filters (Optional)
"""


class BatchCrud:
    def __init__(self, db: Session, batch: int):
        self.res = db.query(Student).filter(Student.Batch == batch)

    def department_filter(self, department: str):
        self.res = self.res.filter(Student.Department == department)
        return self

    def semester_filter(self, semester: int):
        self.res = self.res.filter(Subject.Semester == semester)
        return self

    def backlog_filter(self, total_thres: int, external_thres: int):
        # Needs a Number that tries to request how many marks are required
        # At Minimim
        self.res = (
            self.res.join(Student.Scores)
            .filter(
                or_(
                    (Score.Internals + Score.Externals) < total_thres,
                    Score.Externals < external_thres,
                )
            )
            .options(contains_eager(Student.Scores))
        )
        return self

    def export_usn_list(self, detain: bool = False, detain_thres: int = 4) -> List[str]:
        if detain:
            return [
                x.Usn
                for x in [StudentReport.from_orm(y) for y in self.res]
                if len(x.Scores) >= detain_thres
            ]
        else:
            return [x.Usn for x in self.res]

    def export_student_report(
        self, detain: bool = False, detain_thres: int = 4
    ) -> List[StudentReport]:
        if detain:
            return [StudentReport.from_orm(x) for x in self.res]
        else:
            return [StudentReport.from_orm(x) for x in self.res]

