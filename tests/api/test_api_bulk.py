from fastapi.testclient import TestClient

from semesterstat.reports import (
    DepartmentReport,
    ScoreReport,
    StudentReport,
    SubjectReport,
)


def test_bulk_score(client: TestClient):
    data = [
        ScoreReport(
            Usn="1CR15CS101", SubjectCode="15CS54", Internals=30, Externals=50
        ).dict()
    ]
    res = client.post("/bulk/score", json=data)

    assert res.status_code == 201


def test_bulk_dept(client: TestClient):
    data = [DepartmentReport(Code="XS", Name="E").dict()]
    res = client.post("/bulk/dept", json=data)

    assert res.status_code == 201


def test_bulk_student(client: TestClient):
    data = [StudentReport(Name="XS", Usn="1CR16CS001").dict()]
    res = client.post("/bulk/student", json=data)

    assert res.status_code == 201


def test_bulk_subject(client: TestClient):
    data = [
        SubjectReport(
            Name="X", Code="15CS41", MinExt=21, MinTotal=40, MaxTotal=100, Credits=4
        ).dict()
    ]
    res = client.post("/bulk/subject", json=data)

    assert res.status_code == 201
