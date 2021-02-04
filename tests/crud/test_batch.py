from collections import Counter
from contextlib import nullcontext as does_not_raise
from typing import List, Tuple

import pytest
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from semesterstat.crud.batch import (
    get_all_batch,
    get_batch_backlog,
    get_batch_detained,
    get_batch_scores,
    is_batch_exists,
)


@pytest.mark.parametrize(["batch", "op"], [(2015, True), (2016, True), (2014, False)])
def test_batch_exists(db: Session, batch: int, op: int):
    assert is_batch_exists(db, batch) == op


@pytest.mark.parametrize(
    ["batch", "dept", "sem", "opusn", "opsubcode", "expectation"],
    [
        (
            2015,
            None,
            None,
            ["1CR15CS101", "1CR15CS102"],
            ["15CS65", "15CS64", "15CS54"],
            does_not_raise(),
        ),
        (2014, None, None, [], [], pytest.raises(NoResultFound)),
        (2015, "CS", 6, ["1CR15CS101"], ["15CS65", "15CS64"], does_not_raise()),
    ],
)
def test_batch_scores(
    db: Session,
    batch: int,
    dept: str,
    sem: int,
    opusn: List[str],
    opsubcode: List[str],
    expectation,
):
    with expectation:
        res = get_batch_scores(db, batch, dept, sem)
        assert Counter(opusn) == Counter([x.Usn for x in res])
        assert Counter(opsubcode) == Counter(
            [y.SubjectCode for x in res for y in x.Scores]
        )


@pytest.mark.parametrize(
    ["batch", "dept", "sem", "op", "expectation"],
    [
        (2015, "CS", None, [("1CR15CS101", "15CS64")], does_not_raise()),
        (2017, "CS", None, [("1CR17CS102", "17CS55")], does_not_raise()),
        (2014, None, None, None, pytest.raises(NoResultFound)),
    ],
)
def test_batch_backlog(
    db: Session, batch: int, dept: str, sem: int, op: List[Tuple[str, int]], expectation
):
    with expectation:
        res = get_batch_backlog(db, batch, dept, sem)

        assert res[0].Usn == op[0][0]
        assert res[0].Scores[0].SubjectCode == op[0][1]


@pytest.mark.parametrize(
    ["batch", "dept", "sem", "op", "expectation"],
    [
        (2015, "CS", None, [("1CR15CS101", "15CS64")], does_not_raise()),
        (2017, "CS", None, [("1CR17CS102", "17CS55")], does_not_raise()),
        (2014, None, None, None, pytest.raises(NoResultFound)),
    ],
)
def test_batch_detained(
    db: Session, batch: int, dept: str, sem: int, op: List[Tuple[str, int]], expectation
):
    with expectation:
        res = get_batch_detained(db, batch, dept, thresh=0)

        assert res[0].Usn == op[0][0]
        assert res[0].Scores[0].SubjectCode == op[0][1]


def test_all_batch(db: Session):
    res = get_all_batch(db)

    assert Counter(res) == Counter([2015, 2016, 2017])
