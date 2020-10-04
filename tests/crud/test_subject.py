from collections import Counter
from contextlib import nullcontext as does_not_raise
from typing import List

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from semesterstat.crud.subject import (
    get_subject,
    get_subjects,
    is_subject_exist,
    is_subjects_exists,
    put_subject,
    update_subject,
)
from semesterstat.reports import SubjectReport


@pytest.mark.parametrize(
    ["subcode", "op"],
    [
        ("15CS65", "X"),
        ("15CS64", "X"),
        ("15CS54", "X"),
        ("17MAT11", "X"),
        ("17CSL76", "X"),
        ("17CS55", "X"),
    ],
)
def test_get_subject(db: Session, subcode: str, op: str) -> None:
    assert get_subject(db, subcode).Name == op


@pytest.mark.parametrize(
    ["subcode", "op"],
    [
        ("15CS65", True),
        ("15CS65", True),
        ("15CS54", True),
        ("17MAT11", True),
        ("17CSL76", True),
        ("17CS55", True),
        ("17MAT21", False),
        ("17CSL66", False),
        ("17CS45", False),
    ],
)
def test_is_subject_exists(db: Session, subcode: str, op: bool):
    assert is_subject_exist(db, subcode) == op


@pytest.mark.parametrize(
    ["subcodes", "op"],
    [
        (["15CS65", "15CS64"], True),
        (["15CS65", "15CS64", "15CS54"], True),
        (["15CS65", "15CS64", "15CS54", "19MAT23"], False),
        (["15CS65", "15CS64", "18MAT22"], False),
    ],
)
def test_is_subjects_exist(db: Session, subcodes: List[str], op: bool):
    assert is_subjects_exists(db, subcodes) == op


@pytest.mark.parametrize(
    ["subcode", "expectation"],
    [
        ("10CS11", does_not_raise()),
        ("15CS65", pytest.raises(IntegrityError)),
        ("None", pytest.raises(AttributeError)),
    ],
)
def test_put_student(db: Session, subcode: str, expectation) -> None:
    with expectation:
        put_subject(db, SubjectReport(Code=subcode, Name="EM11"))


@pytest.mark.parametrize(
    ["subcode", "newsubcode", "expectation"],
    [
        ("15CS54", "15CS11", does_not_raise()),
        ("15CS54", "15CS65", pytest.raises(IntegrityError)),
        (None, "15CS65", pytest.raises(AttributeError)),
    ],
)
def test_update_student(
    db: Session, subcode: str, newsubcode: str, expectation
) -> None:
    with expectation:
        update_subject(db, subcode, SubjectReport(Code=newsubcode, Name="EM11"))


@pytest.mark.parametrize(
    ["batch", "dept", "sem", "op"],
    [
        (
            None,
            None,
            None,
            ["15CS65", "15CS64", "15CS54", "17MAT11", "17CSL76", "17CS55"],
        ),
        (2015, None, None, ["15CS65", "15CS64", "15CS54"]),
        (None, "CS", None, ["15CS65", "15CS64", "15CS54", "17CSL76", "17CS55"]),
        (None, None, 6, ["15CS65", "15CS64"]),
        (None, "XX", None, ["17MAT11"]),
        (None, None, 1, ["17MAT11"]),
    ],
)
def test_get_subjects(
    db: Session, batch: int, dept: str, sem: int, op: List[str]
) -> None:
    res = get_subjects(db, batch, dept, sem)

    assert Counter(res) == Counter(op)
