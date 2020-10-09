import pytest
from fastapi.testclient import TestClient
from pydantic.error_wrappers import ValidationError

from semesterstat.reciepts import ScoreReciept, StudentReciept
from semesterstat.reports import StudentReport


@pytest.mark.parametrize(
    ["usn", "rescode", "obj"],
    [
        (
            "1CR15CS101",
            200,
            StudentReciept(
                Name="Mattie Schultz", Usn="1CR15CS101", Batch=2015, Department="CS"
            ),
        ),
        ("1CR15CS001", 404, {"detail": "Student does not Exist"}),
    ],
)
def test_student_get(client: TestClient, usn: str, rescode: int, obj):
    res = client.get("/student/{}".format(usn))

    assert res.status_code == rescode
    try:
        assert StudentReciept(**res.json()) == obj
    except ValidationError:
        assert res.json() == obj


@pytest.mark.parametrize(
    ["usn", "sem", "rescode", "obj"],
    [
        (
            "1CR15CS101",
            None,
            200,
            [
                ScoreReciept(
                    SubjectCode="15CS65",
                    Usn="1CR15CS101",
                    Internals=12,
                    Externals=42,
                ),
                ScoreReciept(
                    SubjectCode="15CS64", Usn="1CR15CS101", Internals=16, Externals=15
                ),
            ],
        ),
        (
            "1CR15CS101",
            6,
            200,
            [
                ScoreReciept(
                    SubjectCode="15CS65",
                    Usn="1CR15CS101",
                    Internals=12,
                    Externals=42,
                ),
                ScoreReciept(
                    SubjectCode="15CS64", Usn="1CR15CS101", Internals=16, Externals=15
                ),
            ],
        ),
        (
            "1CR15CS101",
            5,
            200,
            [],
        ),
        ("1CR15CS001", None, 404, {"detail": "Student does not Exist"}),
    ],
)
def test_student_get_scores_semester(
    client: TestClient, usn: str, sem: int, rescode: int, obj
):
    res = client.get("/student/{}/scores".format(usn), params={"sem": sem})
    assert res.status_code == rescode

    try:
        set([ScoreReciept(**x) for x in res.json()]) == set(obj)
    except (ValidationError, TypeError):
        res.json() == obj


@pytest.mark.parametrize(
    ["usn", "sem", "rescode", "obj"],
    [
        (
            "1CR15CS101",
            None,
            200,
            [
                ScoreReciept(
                    SubjectCode="15CS64", Usn="1CR15CS101", Internals=16, Externals=15
                ),
            ],
        ),
        (
            "1CR15CS101",
            6,
            200,
            [
                ScoreReciept(
                    SubjectCode="15CS64", Usn="1CR15CS101", Internals=16, Externals=15
                ),
            ],
        ),
        (
            "1CR15CS101",
            5,
            200,
            [],
        ),
        ("1CR15CS001", None, 404, {"detail": "Student does not Exist"}),
    ],
)
def test_student_get_backlogs(
    client: TestClient, usn: str, sem: int, rescode: int, obj
):
    res = client.get("/student/{}/backlogs".format(usn), params={"sem": sem})

    assert res.status_code == rescode
    try:
        assert set([ScoreReciept(**x) for x in res.json()]) == set(obj)
    except (ValidationError, TypeError):
        res.json() == obj


@pytest.mark.parametrize(
    ["usn", "subcode", "rescode", "obj"],
    [
        (
            "1CR15CS101",
            "15CS65",
            200,
            ScoreReciept(
                Usn="1CR15CS101", SubjectCode="15CS65", Internals=12, Externals=42
            ),
        ),
        ("1CR15CS101", "15CS66", 404, {"detail": "Subject Not Found"}),
        ("1CR15CS001", "15CS66", 404, {"detail": "Student does not Exist"}),
    ],
)
def test_student_subjectcode(
    client: TestClient, usn: str, subcode: str, rescode: int, obj
):
    res = client.get("/student/{}/subject/{}".format(usn, subcode))

    assert res.status_code == rescode
    try:
        assert ScoreReciept(**res.json()) == obj
    except ValidationError:
        assert res.json() == obj


@pytest.mark.parametrize(
    ["rescode", "iptobj", "ret"],
    [
        (204, StudentReport(Usn="1CR17CS999", Name="Rush"), None),
        (
            409,
            StudentReport(Usn="1CR15CS101", Name="Heck"),
            {"detail": "Student Already Exists"},
        ),
    ],
)
def test_student_post(client: TestClient, rescode: int, iptobj, ret):
    res = client.post("/student/", json=iptobj.dict())
    assert res.status_code == rescode
    assert res.json() == ret


@pytest.mark.parametrize(
    ["usn", "rescode", "iptobj", "ret"],
    [
        ("1CR15CS101", 204, StudentReport(Usn="1CR17CS999", Name="Rush"), None),
        (
            "1CR15CS101",
            409,
            StudentReport(Usn="1CR15CS102", Name="Heck"),
            {"detail": "1CR15CS102 Already Exists"},
        ),
    ],
)
def test_student_put(client: TestClient, usn: str, rescode: int, iptobj, ret):
    res = client.put("/student/{}".format(usn), json=iptobj.dict())

    assert res.status_code == rescode
    assert res.json() == ret
