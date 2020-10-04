from collections import Counter
from contextlib import nullcontext as does_not_raise
from typing import List

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from semesterstat.crud.student import (
    get_student,
    get_student_cgpa,
    get_student_score_credits,
    get_student_scores,
    get_student_scores_by_semester,
    get_student_sgpa,
    get_student_subject,
    get_students,
    is_student_exists,
    put_student,
    update_student,
)
from semesterstat.reports import StudentReport


@pytest.mark.parametrize(
    ["usn", "op"],
    [
        ("1CR15CS101", "X"),
        ("1CR15CS101", "X"),
        ("1CR15CS102", "X"),
        ("1CR17TE102", "X"),
        ("1CR17TE102", "X"),
        ("1CR17CS102", "X"),
    ],
)
def test_get_student(db: Session, usn: str, op: str):
    assert get_student(db, usn).Name == op


@pytest.mark.parametrize(
    ["batch", "dept", "op"],
    [
        (None, None, ["1CR15CS101", "1CR15CS102", "1CR17TE102", "1CR17CS102"]),
        (2015, None, ["1CR15CS101", "1CR15CS102"]),
        (2015, "TE", []),
        (None, "CS", ["1CR15CS101", "1CR15CS102", "1CR17CS102"]),
        (2015, "CS", ["1CR15CS101", "1CR15CS102"]),
        (2017, "CS", ["1CR17CS102"]),
        (2014, "XE", []),
        (None, "TE", ["1CR17TE102"]),
    ],
)
def test_get_students(db: Session, batch: int, dept: str, op: List[str]):
    res = get_students(db, batch, dept)
    assert Counter(res) == Counter(op)


@pytest.mark.parametrize(
    ["usn", "ssb"],
    [
        ("1CR15CS101", ["15CS65", "15CS64"]),
        ("1CR15CS102", ["15CS54"]),
        ("1CR17TE102", ["17MAT11", "17CSL76"]),
        ("1CR17CS102", ["17CS55"]),
        ("1CR17CS120", []),
    ],
)
def test_get_student_scores(db: Session, usn: str, ssb: List[str]):
    res = get_student_scores(db, usn)
    assert Counter([x.SubjectCode for x in res]) == Counter(ssb)


@pytest.mark.parametrize(
    ["usn", "sem", "ssb"],
    [
        ("1CR15CS101", 6, ["15CS65", "15CS64"]),
        ("1CR15CS101", 5, []),
        ("1CR15CS102", 5, ["15CS54"]),
        ("1CR15CS102", 6, []),
        ("1CR17TE102", 1, ["17MAT11"]),
        ("1CR17TE102", 7, ["17CSL76"]),
        ("1CR17CS102", 5, ["17CS55"]),
    ],
)
def test_get_student_scores_by_semester(
    db: Session, usn: str, sem: int, ssb: List[str]
):
    res = get_student_scores_by_semester(db, usn, sem)
    assert Counter([x.SubjectCode for x in res]) == Counter(ssb)


@pytest.mark.parametrize(
    ["usn", "subcode", "internal", "external"],
    [
        ("1CR15CS101", "15CS65", 12, 42),
        ("1CR15CS101", "15CS64", 16, 15),
        ("1CR15CS102", "15CS54", 19, 29),
        ("1CR17TE102", "17MAT11", 19, 55),
        ("1CR17TE102", "17CSL76", 38, 26),
        ("1CR17CS102", "17CS55", 28, 20),
    ],
)
def test_student_subject(
    db: Session, usn: str, subcode: str, internal: int, external: int
):
    res = get_student_subject(db, usn, subcode)
    assert (res.Internals, res.Externals) == (internal, external)


def test_get_student_backlogs(db: Session):
    pass


@pytest.mark.parametrize(
    ["usn", "op"],
    [
        ("1CR15CS101", True),
        ("1CR10CS101", False),
        ("1CR10CS101", False),
        ("1CR17CS102", True),
    ],
)
def test_is_student(db: Session, usn: str, op: bool):
    assert is_student_exists(db, usn) == op


@pytest.mark.parametrize(
    ["usn", "expectation"],
    [("1CR15CS001", does_not_raise()), ("1CR15CS101", pytest.raises(IntegrityError))],
)
def test_put_student(db: Session, usn: str, expectation):
    with expectation:
        put_student(db, StudentReport(Usn=usn, Name="XX"))


@pytest.mark.parametrize(
    ["usn", "newusn", "expectation"],
    [
        ("1CR15CS101", "1CR15CS001", does_not_raise()),
        ("1CR15CS101", "1CR15CS102", pytest.raises(IntegrityError)),
        (None, "1CR15CS101", pytest.raises(AttributeError)),
    ],
)
def test_update_student(db: Session, usn: str, newusn: str, expectation):
    with expectation:
        update_student(db, usn, StudentReport(Usn=newusn, Name="XX"))


@pytest.mark.parametrize(
    ["usn", "subcode", "op"],
    [
        ("1CR15CS101", "15CS65", ((12 + 42) // 10) * 4),
        ("1CR15CS101", "15CS64", ((16 + 15) // 10) * 4),
        ("1CR15CS102", "15CS54", ((19 + 29) // 10) * 4),
        ("1CR17TE102", "17MAT11", ((19 + 55) // 10) * 4),
        ("1CR17TE102", "17CSL76", ((38 + 26) // 10) * 2),
        ("1CR17CS102", "17CS55", ((28 + 20) // 10) * 4),
    ],
)
def test_credits(db: Session, usn: str, subcode: str, op: int):
    assert get_student_score_credits(db, usn, subcode) == op


@pytest.mark.parametrize(
    ["usn", "sem", "op"],
    [("1CR15CS101", 6, 4.00), ("1CR17CS102", 6, 0.0), ("1CR17CS102", 5, 4.00)],
)
def test_student_sgpa(db: Session, usn: str, sem: int, op: float):
    assert get_student_sgpa(db, usn, sem) == pytest.approx(op)


@pytest.mark.parametrize(
    ["usn", "op"], [("1CR15CS101", 4.00), ("1CR15CS102", 4.00), ("1CR17TE102", 6.5)]
)
def test_student_cgpa(db: Session, usn: str, op: float):
    assert get_student_cgpa(db, usn) == pytest.approx(op)
