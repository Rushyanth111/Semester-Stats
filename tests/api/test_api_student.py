import pytest
from fastapi.testclient import TestClient
from jsonschema import validate

from semesterstat.reciepts import ScoreReciept, StudentReciept
from semesterstat.reports import StudentReport


@pytest.mark.parametrize(
    ["usn", "rescode"],
    [("1CR15CS101", 200), ("1CR15CS001", 404)],
)
def test_student_get(client: TestClient, usn: str, rescode: int):
    res = client.get("/student/{}".format(usn))
    assert res.status_code == rescode

    data = res.json()
    if rescode == 200:
        validate(data, StudentReciept.schema())
    elif rescode == 404:
        data == {"detail": "Student Does Not Exist"}


@pytest.mark.parametrize(
    ["usn", "sem", "rescode"],
    [
        ("1CR15CS101", None, 200),
        ("1CR15CS101", 6, 200),
        ("1CR15CS101", 5, 200),
        ("1CR15CS001", None, 404),
    ],
)
def test_student_get_scores_semester(
    client: TestClient, usn: str, sem: int, rescode: int
):
    res = client.get("/student/{}/scores".format(usn), params={"sem": sem})
    assert res.status_code == rescode

    data = res.json()
    if rescode == 200:
        for item in data:
            validate(item, ScoreReciept.schema())
    elif rescode == 404:
        data == {"detail": "Student Does Not Exist"}


@pytest.mark.parametrize(
    ["usn", "sem", "rescode"],
    [
        ("1CR15CS101", None, 200),
        ("1CR15CS101", 6, 200),
        ("1CR15CS101", 5, 200),
        ("1CR15CS001", None, 404),
    ],
)
def test_student_get_backlogs(client: TestClient, usn: str, sem: int, rescode: int):
    res = client.get("/student/{}/backlogs".format(usn), params={"sem": sem})

    assert res.status_code == rescode

    data = res.json()
    if rescode == 200:
        for item in data:
            validate(item, ScoreReciept.schema())
    elif rescode == 404:
        data == {"detail": "Student Does Not Exist"}


@pytest.mark.parametrize(
    ["usn", "subcode", "rescode"],
    [
        ("1CR15CS101", "15CS65", 200),
        ("1CR15CS101", "15CS66", 404),
        ("1CR15CS001", "15CS66", 404),
    ],
)
def test_student_subjectcode(client: TestClient, usn: str, subcode: str, rescode: int):
    res = client.get("/student/{}/subject/{}".format(usn, subcode))
    assert res.status_code == rescode

    data = res.json()
    if rescode == 200:
        validate(data, ScoreReciept.schema())
    elif rescode == 404:
        data == {"detail": "Student Does Not Exist"}


@pytest.mark.parametrize(
    ["rescode", "iptobj"],
    [
        (204, StudentReport(Usn="1CR17CS999", Name="Rush")),
        (409, StudentReport(Usn="1CR15CS101", Name="Heck")),
    ],
)
def test_student_post(client: TestClient, rescode: int, iptobj: StudentReport):
    res = client.post("/student/", json=iptobj.dict())
    assert res.status_code == rescode
    data = res.json()
    if rescode == 409:
        assert data == {"detail": "{} Already Exists".format(iptobj.Usn)}


@pytest.mark.parametrize(
    ["usn", "rescode", "iptobj"],
    [
        ("1CR15CS101", 204, StudentReport(Usn="1CR17CS999", Name="Rush")),
        ("1CR15CS101", 409, StudentReport(Usn="1CR15CS102", Name="Heck")),
        ("1CR17CS101", 404, StudentReport(Usn="1CR15CS102", Name="Heck")),
    ],
)
def test_student_put(client: TestClient, usn: str, rescode: int, iptobj: StudentReport):
    res = client.put("/student/{}".format(usn), json=iptobj.dict())
    data = res.json()
    assert res.status_code == rescode
    if rescode == 409:
        assert data == {"detail": "{} Already Exists".format(iptobj.Usn)}
    if rescode == 404:
        assert data == {"detail": "Student Does Not Exist"}
