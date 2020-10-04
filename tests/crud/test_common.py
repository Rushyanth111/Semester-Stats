from contextlib import nullcontext as does_not_raise

import pytest
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from semesterstat.crud.common import get_scheme


@pytest.mark.parametrize(
    ["batch", "scheme", "expectation"],
    [
        (2015, 2015, does_not_raise()),
        (2016, 2015, does_not_raise()),
        (2017, 2017, does_not_raise()),
        (2014, None, pytest.raises(NoResultFound)),
        (1, None, pytest.raises(NoResultFound)),
        (None, None, pytest.raises(NoResultFound)),
    ],
)
def test_get_scheme(db: Session, batch: int, scheme: int, expectation):
    with expectation:
        res = get_scheme(db, batch)
        assert res == scheme
