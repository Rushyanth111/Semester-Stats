from typing import Counter, List

import pytest
from sqlalchemy.orm import Session

from semesterstat.common import StudentReport
from semesterstat.crud import (
    get_student,
    get_student_scores,
    get_student_scores_by_semester,
    get_student_subject,
    is_student_exists,
    put_student,
    update_student,
)


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


def test_put_student(db: Session):
    put_student(db, StudentReport(Usn="1CR10CS102", Name="XX"))
    assert is_student_exists(db, "1CR10CS102")


def test_update_student(db: Session):
    update_student(
        db, "1CR15CS101", StudentReport(Usn="1CR10CS102", Name="XX"),
    )
    assert is_student_exists(db, "1CR10CS102")
