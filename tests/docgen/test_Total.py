import json
from contextlib import nullcontext as does_not_raise

import pytest
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from semesterstat.crud.summary import MainSummary

with open("tests/data/data.json") as f:
    data = json.load(f)


@pytest.mark.parametrize(
    ["batch", "dept", "sem", "countdata", "expectation"],
    [
        (
            data["static"]["Batch"],
            data["static"]["Dept"],
            data["static"]["Semester"],
            data["data"],
            does_not_raise(),
        )
    ]
    + [
        (None, None, None, None, pytest.raises(NoResultFound)),
        (2014, None, None, None, pytest.raises(NoResultFound)),
        (None, "None", None, None, pytest.raises(NoResultFound)),
        (None, None, 9, None, pytest.raises(NoResultFound)),
    ],
)
class TestSummary:
    def test_appeared(
        self, db: Session, batch: int, dept: str, sem: int, countdata: int, expectation
    ):
        with expectation:
            res = MainSummary(db, batch, dept, sem)
            assert res.get_appeared() == countdata["Appeared"]

    def test_fail(
        self, db: Session, batch: int, dept: str, sem: int, countdata: int, expectation
    ):
        with expectation:
            res = MainSummary(db, batch, dept, sem)
            assert res.get_fail() == countdata["Fail"]

    def test_fcd(
        self, db: Session, batch: int, dept: str, sem: int, countdata: int, expectation
    ):
        with expectation:
            res = MainSummary(db, batch, dept, sem)
            assert res.get_fcd() == countdata["FCD"]

    def test_fc(
        self, db: Session, batch: int, dept: str, sem: int, countdata: int, expectation
    ):
        with expectation:
            res = MainSummary(db, batch, dept, sem)
            assert res.get_fc() == countdata["FC"]

    def test_sc(
        self, db: Session, batch: int, dept: str, sem: int, countdata: int, expectation
    ):
        with expectation:
            res = MainSummary(db, batch, dept, sem)
            assert res.get_sc() == countdata["SC"]
