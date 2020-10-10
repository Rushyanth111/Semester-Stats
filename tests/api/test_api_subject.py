import pytest
from fastapi.testclient import TestClient
from jsonschema import validate

from semesterstat.reciepts import SubjectReciept
from semesterstat.reports import SubjectReport


@pytest.mark.parametrize(["subcode", "rescode"], [("15CS64", 200), ("15CS66", 404)])
def test_subject_get(client: TestClient, subcode: str, rescode: int):
    res = client.get("/subject/{}".format(subcode))
    assert res.status_code == rescode

    data = res.json()
    if rescode == 200:
        validate(data, SubjectReciept.schema())
    elif rescode == 404:
        data == {"detail": "Subject Does Not Exist"}


@pytest.mark.parametrize(["subcode", "rescode"], [("15CS66", 201), ("15CS64", 409)])
def test_subject_insert(client: TestClient, subcode: str, rescode: int):
    data = SubjectReport(
        Name="X", Code=subcode, MinExt=21, MinTotal=40, MaxTotal=100, Credits=4
    ).dict()

    res = client.post("/subject/", json=data)

    assert res.status_code == rescode


@pytest.mark.parametrize(
    ["subcode", "subcodenew", "rescode"],
    [("15CS65", "15CS66", 201), ("15CS65", "15CS64", 409)],
)
def test_subject_update(
    client: TestClient, subcode: str, subcodenew: str, rescode: int
):
    data = SubjectReport(
        Name="X", Code=subcodenew, MinExt=21, MinTotal=40, MaxTotal=100, Credits=4
    ).dict()

    res = client.put("/subject/{}".format(subcode), json=data)

    assert res.status_code == rescode
