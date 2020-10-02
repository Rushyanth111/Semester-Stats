from collections import Counter
from typing import List

import pytest
from sqlalchemy.orm import Session

from semesterstat.common.reports import DepartmentReport
from semesterstat.crud.dept import (
    get_all_dept,
    get_dept_by_code,
    get_dept_by_name,
    get_dept_students,
    get_dept_subjects,
    is_dept_exist,
    put_department,
    update_department,
)


@pytest.mark.parametrize(
    ["dept", "op"],
    [
        ("CS", "Computer Science"),
        ("IS", "Information Science"),
        ("TE", "Telecommunication"),
        ("ME", "Mechanical Engineering"),
        ("AE", "Aeronautical Engineering"),
    ],
)
def test_get_dept_by_code(db: Session, dept: str, op: str):
    assert get_dept_by_code(db, dept).Name == op


@pytest.mark.parametrize(
    ["deptcode", "name"],
    [
        ("CS", "Computer Science"),
        ("IS", "Information Science"),
        ("TE", "Telecommunication"),
        ("ME", "Mechanical Engineering"),
        ("AE", "Aeronautical Engineering"),
    ],
)
def test_dept_by_name(db: Session, deptcode: str, name: str):
    assert get_dept_by_name(db, name).Code == deptcode


@pytest.mark.parametrize(
    ["dept", "op"],
    [
        ("CS", ["1CR15CS102", "1CR15CS101", "1CR17CS102"]),
        ("TE", ["1CR17TE102"]),
        ("AE", []),
    ],
)
def test_get_dept_students(db: Session, dept: str, op: List[str]):
    res = get_dept_students(db, dept)
    assert Counter([x.Usn for x in res]) == Counter(op)


@pytest.mark.parametrize(
    ["dept", "scheme", "op"],
    [
        ("CS", None, ["15CS65", "15CS64", "15CS54", "17CSL76", "17CS55"]),
        ("CS", 2015, ["15CS65", "15CS64", "15CS54"]),
        ("CS", 2017, ["17CSL76", "17CS55"]),
        ("CS", 2018, []),
        ("TE", None, []),
        ("XX", None, ["17MAT11"]),
    ],
)
def test_get_dept_subject(db: Session, dept: str, scheme: int, op: List[str]):
    res = get_dept_subjects(db, dept, scheme)
    assert Counter([x.Code for x in res]) == Counter(op)


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


def test_put_dept(db: Session):
    put_department(db, DepartmentReport(Code="1A", Name="OSOSOS"))

    assert is_dept_exist(db, "1A")


def test_update_department(db: Session):
    update_department(
        db, "CS", DepartmentReport(Code="XC", Name="OSD"),
    )
    assert is_dept_exist(db, "XC")


def test_all_dept(db: Session):
    res = get_all_dept(db)

    assert Counter(["CS", "IS", "TE", "ME", "AE"]) == Counter(res)
