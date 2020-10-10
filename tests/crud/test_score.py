import pytest
from sqlalchemy.orm.session import Session

from semesterstat.crud.score import is_scores_exist


@pytest.mark.parametrize(
    ["batch", "sem", "dept", "op"],
    [
        (2015, 6, None, True),
        (2015, 6, "CS", True),
        (2015, 6, "TE", False),
        (2014, None, None, False),
    ],
)
def test_is_scores_exists(db: Session, batch: int, sem: int, dept: str, op: bool):
    res = is_scores_exist(db, batch, sem, dept)

    assert res == op
