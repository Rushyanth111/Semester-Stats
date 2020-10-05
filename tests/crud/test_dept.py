from collections import Counter
from contextlib import nullcontext as does_not_raise

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from semesterstat.crud.dept import (
    get_all_dept,
    get_dept_by_code,
    is_dept_exist,
    put_department,
    update_department,
)
from semesterstat.reports import DepartmentReport


@pytest.mark.parametrize(
    ["dept", "op", "expectation"],
    [
        ("CS", "Computer Science", does_not_raise()),
        ("IS", "Information Science", does_not_raise()),
        ("12", None, pytest.raises(NoResultFound)),
    ],
)
def test_get_dept_by_code(db: Session, dept: str, op: str, expectation):
    with expectation:
        assert get_dept_by_code(db, dept).Name == op


@pytest.mark.parametrize(
    ["dept", "op"],
    [
        ("CS", True),
        ("IS", True),
        ("TE", True),
        ("ME", True),
        ("AE", True),
        ("DS", False),
        ("SS", False),
        ("12", False),
    ],
)
def test_is_dept_exists(db: Session, dept: str, op: bool):
    assert is_dept_exist(db, dept) == op


@pytest.mark.parametrize(
    ["dept", "expectation"],
    [
        ("1A", does_not_raise()),
        ("CS", pytest.raises(IntegrityError)),
    ],
)
def test_put_dept(db: Session, dept: str, expectation):
    with expectation:
        put_department(db, DepartmentReport(Code=dept, Name="X"))


@pytest.mark.parametrize(
    ["dept", "newdept", "expectation"],
    [
        ("CS", "1A", does_not_raise()),
        ("CS", "TE", pytest.raises(IntegrityError)),
    ],
)
def test_update_department(db: Session, dept: str, newdept: str, expectation):
    with expectation:
        update_department(db, dept, DepartmentReport(Code=newdept, Name="X"))


def test_all_dept(db: Session):
    res = get_all_dept(db)

    assert Counter(["CS", "IS", "TE", "ME", "AE"]) == Counter(res)
