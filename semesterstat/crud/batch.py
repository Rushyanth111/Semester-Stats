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

    def detained_filter(self, total_fail_threshold: int, external_fail_threshold: int):
        # Needs a Number that tries to request how many marks are required
        # At Minimim
        self.res = self.res.filter(
            or_(
                (Score.Internals + Score.Externals) < total_fail_threshold,
                Score.Externals < external_fail_threshold,
            )
        ).where(func.count(Score.SubjectCode) > 4)
        return self

    def backlog_filter(self, total_fail_threshold: int, external_fail_threshold: int):
        # Needs a Number that tries to request how many marks are required
        # At Minimim
        self.res = (
            self.res.join(Student.Scores)
            .filter(
                or_(
                    (Score.Internals + Score.Externals) < total_fail_threshold,
                    Score.Externals < external_fail_threshold,
                )
            )
            .options(contains_eager(Student.Scores))
        )
        return self

    def export_usn_list(self) -> List[str]:
        return [x for (x,) in self.res.with_entities(Student.Usn)]

    def export_student_report(self) -> List[StudentReport]:
        print([x for x in self.res])
        return [StudentReport.from_orm(x) for x in self.res]


# Requires Specificity Component
