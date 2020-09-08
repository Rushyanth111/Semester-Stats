from collections import Counter
from typing import List, Tuple

import pytest
from sqlalchemy.orm.session import Session

from semesterstat.crud import (
    get_batch_aggregate,
    get_batch_scores,
    get_batch_students,
    get_batch_students_usn,
    get_batch_backlog,
    get_scheme,
    is_batch_exists,
    get_batch_detained_students,
)


@pytest.mark.parametrize(
    ["batch", "scheme"], [(2015, 2015), (2016, 2015), (2017, 2017)]
)
def test_get_scheme(db: Session, batch: int, scheme: int):
    res = get_scheme(db, batch)
    assert res == scheme


@pytest.mark.parametrize(["batch", "op"], [(2015, True), (2016, True), (2014, False)])
def test_batch_exists(db: Session, batch: int, op: int):
    assert is_batch_exists(db, batch) == op


@pytest.mark.parametrize(
    ["batch", "dept", "op"],
    [
        (2015, None, ["1CR15CS101", "1CR15CS102"]),
        (2015, "CS", ["1CR15CS101", "1CR15CS102"]),
        (2015, "TE", []),
    ],
)
def test_batch_students(db: Session, batch: int, dept: str, op: List[str]):
    res = get_batch_students(db, batch, dept)
    assert [x.Usn for x in res] == op


@pytest.mark.parametrize(
    ["batch", "dept", "op"],
    [
        (2015, None, ["1CR15CS101", "1CR15CS102"]),
        (2015, "CS", ["1CR15CS101", "1CR15CS102"]),
        (2015, "TE", []),
    ],
)
def test_batch_students_usn(db: Session, batch: int, dept: str, op: List[str]):
    assert get_batch_students_usn(db, batch, dept) == op


@pytest.mark.parametrize(
    ["batch", "dept", "sem", "opusn", "opsubcode"],
    [
        (
            2015,
            None,
            None,
            ["1CR15CS101", "1CR15CS102"],
            ["15CS65", "15CS64", "15CS54"],
        ),
        (2014, None, None, [], []),
        (2015, "CS", 6, ["1CR15CS101"], ["15CS65", "15CS64"]),
    ],
)
def test_batch_scores(
    db: Session, batch: int, dept: str, sem: int, opusn: List[str], opsubcode: List[str]
):
    res = get_batch_scores(db, batch, dept, sem)

    assert Counter(opusn) == Counter([x.Usn for x in res])
    assert Counter(opsubcode) == Counter([y.SubjectCode for x in res for y in x.Scores])


@pytest.mark.parametrize(
    ["batch", "dept", "op"],
    [
        (2015, "CS", [("1CR15CS101", 85), ("1CR15CS102", 48)]),
        (2016, "CS", []),
        (2017, "TE", [("1CR17TE102", 138)]),
    ],
)
def test_batch_aggregate(db: Session, batch: int, dept: str, op: List[Tuple[str, int]]):
    assert Counter(get_batch_aggregate(db, batch, dept)) == Counter(op)


@pytest.mark.parametrize(
    ["batch", "dept", "sem", "op"],
    [
        (2015, "CS", None, [("1CR15CS101", "15CS64")]),
        (2017, "CS", None, [("1CR17CS102", "17CS55")]),
    ],
)
def test_batch_backlog(
    db: Session, batch: int, dept: str, sem: int, op: List[Tuple[str, int]]
):
    res = get_batch_backlog(db, batch, dept, sem)

    assert res[0].Usn == op[0][0]
    assert res[0].Scores[0].SubjectCode == op[0][1]


@pytest.mark.parametrize(
    ["batch", "dept", "sem", "op"],
    [
        (2015, "CS", None, [("1CR15CS101", "15CS64")]),
        (2017, "CS", None, [("1CR17CS102", "17CS55")]),
    ],
)
def test_batch_detained(
    db: Session, batch: int, dept: str, sem: int, op: List[Tuple[str, int]]
):
    res = get_batch_detained_students(db, batch, dept, thresh=0)

    assert res[0].Usn == op[0][0]
    assert res[0].Scores[0].SubjectCode == op[0][1]
