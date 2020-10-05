from contextlib import nullcontext as does_not_raise

import pytest
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from semesterstat.crud.summary import get_summary


@pytest.mark.dependency(
    depends=[
        "Subject.Summary.Appeared",
        "Subject.Summary.Failed",
        "Subject.Summary.FCD",
        "Subject.Summary.FC",
        "Subject.Summary.SC",
        "Subject.Appeared",
        "Subject.Failed",
        "Subject.FCD",
        "Subject.FC",
        "Subject.SC",
    ]
)
@pytest.mark.parametrize(
    ["batch", "dept", "sem", "expectation"],
    [
        (2015, "CS", 1, does_not_raise()),
        (2014, None, None, pytest.raises(NoResultFound)),
    ],
)
def test_get_summary(db: Session, batch: int, dept: str, sem: int, expectation):
    with expectation:
        get_summary(db, batch, dept, sem)
