from collections import Counter

import pytest
from fastapi.testclient import TestClient
from jsonschema import validate

from semesterstat.reciepts import DepartmentReciept
from semesterstat.reports import DepartmentReport


@pytest.mark.parametrize(
    ["dept", "rescode"],
    [
        ("CS", 200),
        ("XX", 404),
    ],
)
def test_api_get_dept(client: TestClient, dept: str, rescode: int):
    res = client.get("/dept/{}".format(dept))
    assert res.status_code == rescode
    data = res.json()
    if rescode == 200:
        validate(data, DepartmentReciept.schema())
    elif rescode == 404:
        assert data == {"detail": "Dept Does Not Exist"}


@pytest.mark.parametrize(["rescode", "object"], [(200, ["CS", "IS", "TE", "ME", "AE"])])
def test_api_get_all(client: TestClient, rescode: int, object):
    res = client.get("/dept/")
    assert res.status_code == rescode
    assert Counter(res.json()) == Counter(object)


@pytest.mark.parametrize(["deptcode", "rescode"], [("XX", 204), ("CS", 409)])
def test_api_post_dept(client: TestClient, deptcode: str, rescode: int):
    iptobj = DepartmentReport(Code=deptcode, Name="X")

    res = client.post("/dept/", json=iptobj.dict())

    assert res.status_code == rescode
    data = res.json()
    if rescode == 409:
        assert data == {"detail": "{} Already Exists".format(deptcode)}


@pytest.mark.parametrize(
    ["deptcode", "deptcodenew", "rescode"],
    [
        ("XX", "XV", 404),
        ("CS", "XV", 204),
        ("CS", "TE", 409),
    ],
)
def test_api_put_dept(
    client: TestClient, deptcode: str, deptcodenew: str, rescode: int
):
    iptobj = DepartmentReport(Code=deptcodenew, Name="X")

    res = client.put("/dept/{}".format(deptcode), json=iptobj.dict())

    assert res.status_code == rescode
    data = res.json()
    if rescode == 409:
        assert data == {"detail": "{} Already Exists".format(deptcodenew)}
    if rescode == 404:
        assert data == {"detail": "Dept Does Not Exist"}
