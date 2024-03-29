from typing import List

from sqlalchemy import func, or_
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from ...database import Score, Student, Subject
from ...plugins import fc, fcd
from ..batch import is_batch_exists
from ..common import get_scheme
from ..dept import is_dept_exist
from ..subject import get_subjects


class MainSummary:
    def __init__(self, db: Session, batch: int, dept: str, sem: int):
        if not is_batch_exists(db, batch) or not is_dept_exist(db, dept):
            raise NoResultFound

        scheme = get_scheme(db, batch)

        __usns = db.query(Student.Usn).filter(
            Student.Batch == batch, Student.Department == dept
        )

        self.__subject_codes = get_subjects(db, batch=batch, dept=dept, sem=sem)

        self.__appeared = (
            db.query(Score.Usn)
            .filter(Score.Usn.in_(__usns), Score.SubjectCode.in_(self.__subject_codes))
            .distinct()
        )

        __base_fail = (
            db.query(Score.Usn)
            .join(Subject)
            .filter(
                Score.Usn.in_(__usns),
                Score.SubjectCode.in_(self.__subject_codes),
                or_(
                    Score.Externals < Subject.MinExt,
                    (Score.Externals + Score.Internals) < (Subject.MinTotal),
                ),
            )
        ).distinct()

        self.__fail = __base_fail.count()

        # _usns = All USN, __base_fail = USN that have failed one or more subjects
        __usns_pass_list = set([x.Usn for x in self.__appeared]) - set(
            [x.Usn for x in __base_fail]
        )

        self.__appeared = self.__appeared.count()

        self.__pass = len(__usns_pass_list)

        __base_pass = (
            db.query(Score.Usn)
            .filter(
                Score.Usn.in_(__usns_pass_list),
                Score.SubjectCode.in_(self.__subject_codes),
            )
            .group_by(Score.Usn)
        )

        # __subject_sum = (
        #     db.query(func.sum(Subject.MaxTotal))
        #     .filter(Subject.Code.in_(self.__subject_codes))
        #     .scalar()
        # )

        # BUG: There's actually no way of determining which of the electives that
        # students have taken Which means that I can approximate the fact the each
        # of the semesters have exactly 800.
        # This is a temporary fix, Needs to be better approximated.
        # Ideally, I'll Fix this in a later iteration.

        if sem in [1, 2, 3, 4, 5, 6, 7]:
            __subject_sum = 800
        else:
            __subject_sum = 600
        # print("ABBBA", __subject_sum, self.__subject_codes)

        self.__fcd = __base_pass.having(
            fcd(scheme, func.sum(Score.Externals + Score.Internals), __subject_sum)
        ).count()

        self.__fc = __base_pass.having(
            fc(scheme, func.sum(Score.Externals + Score.Internals), __subject_sum)
        ).count()

        self.__sc = self.__pass - self.__fcd - self.__fc

        try:
            self.__pass_percent = self.__pass / self.__appeared
        except ZeroDivisionError:
            self.__pass_percent = 0.0

    def get_appeared(self) -> int:
        return self.__appeared

    def get_fcd(self) -> int:
        return self.__fcd

    def get_fc(self) -> int:
        return self.__fc

    def get_sc(self) -> int:
        return self.__sc

    def get_pass(self) -> int:
        return self.__pass

    def get_fail(self) -> int:
        return self.__fail

    def get_pass_percent(self) -> float:
        return float("{:.2f}".format(self.__pass_percent))

    def get_subjects(self) -> List[str]:
        return self.__subject_codes

    Appeared = property(get_appeared)
    Fcd = property(get_fcd)
    Fc = property(get_fc)
    Sc = property(get_sc)
    Pass = property(get_pass)
    Fail = property(get_fail)
    PassPercent = property(get_pass_percent)
