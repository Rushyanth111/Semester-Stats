import pytest
from sqlalchemy.orm.session import Session
from semesterstat.crud import get_scheme


@pytest.mark.parametrize(
    ["batch", "scheme"],
    [(2015, 2015), (2016, 2015), (2017, 2017), (2014, None), (1, None), (None, None)],
)
def test_get_scheme(db: Session, batch: int, scheme: int):
    res = get_scheme(db, batch)
    assert res == scheme
