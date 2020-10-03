from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from ...crud.common import get_scheme
from ...crud.subject import get_subjects
from ...database import Score, Student, Subject
from ...plugins import fc, fcd


class MainSummary:
    def __init__(self, db: Session, batch: int, dept: str, sem: int):

        scheme = get_scheme(db, batch)

        __usns = db.query(Student.Usn).filter(
            Student.Batch == batch, Student.Department == dept
        )

        __subject_codes = get_subjects(db, batch=batch, dept=dept, sem=sem)

        self.__appeared = (
            db.query(Score.Usn)
            .filter(Score.Usn.in_(__usns), Score.SubjectCode.in_(__subject_codes))
            .distinct()
        )

        __base_fail = (
            db.query(Score.Usn)
            .join(Subject)
            .filter(
                Score.Usn.in_(__usns),
                Score.SubjectCode.in_(__subject_codes),
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
                Score.Usn.in_(__usns_pass_list), Score.SubjectCode.in_(__subject_codes)
            )
            .group_by(Score.Usn)
        )

        __subject_sum = (
            db.query(func.sum(Subject.MaxTotal))
            .filter(Subject.Code.in_(__subject_codes))
            .scalar()
        )

        self.__fcd = __base_pass.having(
            fcd(scheme, func.sum(Score.Externals + Score.Internals), __subject_sum)
        ).count()

        self.__fc = __base_pass.having(
            fc(scheme, func.sum(Score.Externals + Score.Internals), __subject_sum)
        ).count()

        self.__sc = self.__pass - self.__fcd - self.__fc

        self.__pass_percent = self.__pass / self.__appeared

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

    def get_pass_percent(self) -> int:
        return self.__pass_percent
