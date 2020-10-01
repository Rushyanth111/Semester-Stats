"""
Given: Subject Code, Batch, Dept

To Determine:

Teachers Name -> Obtain from Teacher Table: Not present
Appeared -> Number of Students Appeared in that exam.
Fail -> Number of Students that have failed
FCD -> Number of Students that have an FCD
FC -> Number of Students that have an FC
SC -> Number of Students that have an SC
Pass Percentage -> Percentage of Pass.
"""

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from ..database import Score, Student, Subject
from ..plugins import fc, fcd, sc
from ..crud import get_scheme


class SubjectFill:
    def __init__(self, db: Session, subcode: str, batch: int, dept: str) -> None:
        scheme = get_scheme(db, batch)

        __usns = db.query(Student.Usn).filter(
            Student.Batch == batch, Student.Department == dept
        )

        __base = (
            db.query(Score)
            .join(Subject)
            .filter(Score.SubjectCode == subcode, Score.Usn.in_(__usns))
        )

        self.__appeared = __base.count()
        self.__failed = __base.filter(
            or_(
                Score.Externals < Subject.MinExt,
                (Score.Externals + Score.Internals) < (Subject.MinTotal),
            )
        ).count()

        __base_pass = __base.filter(
            and_(
                Score.Externals >= Subject.MinExt,
                (Score.Externals + Score.Internals) >= (Subject.MinTotal),
            )
        )

        self.__fcd = __base_pass.filter(
            fcd(scheme, Score.Externals + Score.Internals, Subject.MaxTotal)
        ).count()

        self.__fc = __base_pass.filter(
            fc(scheme, Score.Externals + Score.Internals, Subject.MaxTotal)
        ).count()

        self.__sc = __base_pass.filter(
            sc(scheme, Score.Externals + Score.Internals, Subject.MaxTotal)
        ).count()

        try:
            self.__pass_percentage = (1 - self.__failed / self.__appeared) * 100
        except ZeroDivisionError:
            self.__pass_percentage = 0

    def get_appeared(self) -> int:
        return self.__appeared

    def get_failed(self) -> int:
        return self.__failed

    def get_fcd(self) -> int:
        return self.__fcd

    def get_fc(self) -> int:
        return self.__fc

    def get_sc(self) -> int:
        return self.__sc

    def get_pass_percent(self) -> int:
        return self.__pass_percentage
