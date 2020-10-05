import json

import pytest
from sqlalchemy.orm import Session

from semesterstat.crud.summary import SubjectSummary

with open("tests/data/data.json") as f:
    data = json.load(f)


@pytest.mark.dependency(name="Subject.Summary.Appeared")
@pytest.mark.parametrize(
    ["subcode", "batch", "dept", "count"],
    [
        (k, data["static"]["Batch"], data["static"]["Dept"], v["Appeared"])
        for (k, v) in data["data"]["SubData"].items()
    ],
)
def test_appeared(db: Session, subcode: str, batch: int, dept: str, count: int):
    res = SubjectSummary(db, subcode, batch, dept)
    assert res.get_appeared() == count


@pytest.mark.dependency(name="Subject.Summary.Failed")
@pytest.mark.parametrize(
    ["subcode", "batch", "dept", "count"],
    [
        (k, data["static"]["Batch"], data["static"]["Dept"], v["Fail"])
        for (k, v) in data["data"]["SubData"].items()
    ],
)
def test_failed(db: Session, subcode: str, batch: int, dept: str, count: int):
    res = SubjectSummary(db, subcode, batch, dept)
    assert res.get_failed() == count


@pytest.mark.dependency(name="Subject.Summary.FCD")
@pytest.mark.parametrize(
    ["subcode", "batch", "dept", "count"],
    [
        (k, data["static"]["Batch"], data["static"]["Dept"], v["FCD"])
        for (k, v) in data["data"]["SubData"].items()
    ],
)
def test_fcd(db: Session, subcode: str, batch: int, dept: str, count: int):
    res = SubjectSummary(db, subcode, batch, dept)
    assert res.get_fcd() == count


@pytest.mark.dependency(name="Subject.Summary.FC")
@pytest.mark.parametrize(
    ["subcode", "batch", "dept", "count"],
    [
        (k, data["static"]["Batch"], data["static"]["Dept"], v["FC"])
        for (k, v) in data["data"]["SubData"].items()
    ],
)
def test_fc(db: Session, subcode: str, batch: int, dept: str, count: int):
    res = SubjectSummary(db, subcode, batch, dept)
    assert res.get_fc() == count


@pytest.mark.dependency(name="Subject.Summary.SC")
@pytest.mark.parametrize(
    ["subcode", "batch", "dept", "count"],
    [
        (k, data["static"]["Batch"], data["static"]["Dept"], v["SC"])
        for (k, v) in data["data"]["SubData"].items()
    ],
)
def test_sc(db: Session, subcode: str, batch: int, dept: str, count: int):
    res = SubjectSummary(db, subcode, batch, dept)
    assert res.get_sc() == count
