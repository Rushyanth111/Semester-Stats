from typing import List

import pytest
from sqlalchemy.orm import Session

from semesterstat.common import SubjectReport
from semesterstat.crud import (
    get_subject,
    is_subject_exist,
    is_subjects_exists,
    put_subject,
    update_subject,
)


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


def test_put_student(db: Session) -> None:
    put_subject(db, SubjectReport(Code="10CS11", Name="EM11"))
    assert is_subject_exist(db, "10CS11")
    db.rollback()


def test_update_student(db: Session) -> None:
    update_subject(
        db, "15CS64", SubjectReport(Code="10CS11", Name="EM11"),
    )
    assert is_subject_exist(db, "10CS11")
    db.rollback()
