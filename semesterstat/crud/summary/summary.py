"""
For a given Batch, Semester and Department, Spit Out a Dict for the Same.
"""

from sqlalchemy.orm import Session

from ...reciepts import SubjectSummaryReciept, SummaryReciept
from .mainqueries import MainSummary
from .subjectqueries import SubjectSummary


def get_summary(db: Session, batch: int, dept: str, sem: int) -> SummaryReciept:
    """Get Summary of the Given Batch

    Args:
        db (Session): SQLAlchemy Session
        batch (int): Batch Filter
        dept (str): Dept Filter
        sem (int): Semester Filter.

    Raises:
        NoResultFound

    Returns:
        SummaryReciept: Reciept of the Summary, No Report, Since it's not Usable.
    """
    main_info = MainSummary(db, batch, dept, sem)
    sub_dict = {}
    subjects = main_info.get_subjects()
    for sub in subjects:
        res = SubjectSummary(db, sub, batch, dept)
        sub_dict[sub] = SubjectSummaryReciept.from_orm(res)

    rep = SummaryReciept.from_orm(main_info)
    rep.Subjects = sub_dict

    return rep
