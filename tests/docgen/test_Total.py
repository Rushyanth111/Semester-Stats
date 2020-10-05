import json

import pytest
from sqlalchemy.orm import Session

from semesterstat.crud.summary import MainSummary

with open("tests/data/data.json") as f:
    data = json.load(f)


@pytest.mark.dependency(name="Summary.Appeared")
@pytest.mark.parametrize(
    ["batch", "dept", "sem", "count"],
    [
        (
            data["static"]["Batch"],
            data["static"]["Dept"],
            data["static"]["Semester"],
            data["data"]["Appeared"],
        )
    ],
)
def test_appeared(db: Session, batch: int, dept: str, sem: int, count: int):
    res = MainSummary(db, batch, dept, sem)

    assert res.get_appeared() == count


@pytest.mark.dependency(name="Summary.Failed")
@pytest.mark.parametrize(
    ["batch", "dept", "sem", "count"],
    [
        (
            data["static"]["Batch"],
            data["static"]["Dept"],
            data["static"]["Semester"],
            data["data"]["Fail"],
        )
    ],
)
def test_fail(db: Session, batch: int, dept: str, sem: int, count: int):
    res = MainSummary(db, batch, dept, sem)

    assert res.get_fail() == count


@pytest.mark.dependency(name="Summary.FCD")
@pytest.mark.parametrize(
    ["batch", "dept", "sem", "count"],
    [
        (
            data["static"]["Batch"],
            data["static"]["Dept"],
            data["static"]["Semester"],
            data["data"]["FCD"],
        )
    ],
)
def test_fcd(db: Session, batch: int, dept: str, sem: int, count: int):
    res = MainSummary(db, batch, dept, sem)

    assert res.get_fcd() == count


@pytest.mark.dependency(name="Summary.FC")
@pytest.mark.parametrize(
    ["batch", "dept", "sem", "count"],
    [
        (
            data["static"]["Batch"],
            data["static"]["Dept"],
            data["static"]["Semester"],
            data["data"]["FC"],
        )
    ],
)
def test_fc(db: Session, batch: int, dept: str, sem: int, count: int):
    res = MainSummary(db, batch, dept, sem)
    assert res.get_fc() == count


@pytest.mark.dependency(name="Summary.SC")
@pytest.mark.parametrize(
    ["batch", "dept", "sem", "count"],
    [
        (
            data["static"]["Batch"],
            data["static"]["Dept"],
            data["static"]["Semester"],
            data["data"]["SC"],
        )
    ],
)
def test_sc(db: Session, batch: int, dept: str, sem: int, count: int):
    res = MainSummary(db, batch, dept, sem)
    assert res.get_sc() == count
