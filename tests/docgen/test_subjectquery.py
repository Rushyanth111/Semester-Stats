import json

import pytest
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from semesterstat.crud.summary import SubjectSummary
from tests.docgen.test_summary import does_not_raise

with open("tests/data/data.json") as f:
    data = json.load(f)


@pytest.mark.parametrize(
    ["batch", "dept", "subcode", "countdata", "expectation"],
    [
        (
            data["static"]["Batch"],
            data["static"]["Dept"],
            subcode,
            data["data"]["SubData"][subcode],
            does_not_raise(),
        )
        for subcode in data["subcode"]
    ]
    + [
        (0, None, None, None, pytest.raises(NoResultFound)),
        (None, "XXX", None, None, pytest.raises(NoResultFound)),
        (None, None, "SOMESD", None, pytest.raises(NoResultFound)),
    ],
)
class TestSubjectSummary:
    def test_appeared(
        self, db: Session, subcode: str, batch: int, dept: str, countdata, expectation
    ):
        with expectation:
            res = SubjectSummary(db, subcode, batch, dept)
            assert res.get_appeared() == countdata["Appeared"]

    def test_failed(
        self, db: Session, subcode: str, batch: int, dept: str, countdata, expectation
    ):
        with expectation:
            res = SubjectSummary(db, subcode, batch, dept)
            assert res.get_failed() == countdata["Fail"]

    def test_fcd(
        self, db: Session, subcode: str, batch: int, dept: str, countdata, expectation
    ):
        with expectation:
            res = SubjectSummary(db, subcode, batch, dept)
            assert res.get_fcd() == countdata["FCD"]

    def test_fc(
        self, db: Session, subcode: str, batch: int, dept: str, countdata, expectation
    ):
        with expectation:
            res = SubjectSummary(db, subcode, batch, dept)
            assert res.get_fc() == countdata["FC"]

    def test_sc(
        self, db: Session, subcode: str, batch: int, dept: str, countdata, expectation
    ):
        with expectation:
            res = SubjectSummary(db, subcode, batch, dept)
            assert res.get_sc() == countdata["SC"]
