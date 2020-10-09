from collections import Counter

import pytest
from fastapi.testclient import TestClient

from semesterstat.reciepts import DepartmentReciept
from semesterstat.reports import DepartmentReport


@pytest.mark.parametrize(
    ["dept", "statuscode", "object"],
    [
        ("CS", 200, DepartmentReciept(Code="CS", Name="Computer Science").dict()),
        (
            "XX",
            404,
            {"detail": "No Such Department"},
        ),
    ],
)
def test_api_get_dept(client: TestClient, dept: str, statuscode: int, object):
    res = client.get("/dept/{}".format(dept))
    data = res.json()
    assert res.status_code == statuscode
    assert data == object


@pytest.mark.parametrize(
    ["statuscode", "object"], [(200, ["CS", "IS", "TE", "ME", "AE"])]
)
def test_api_get_all(client: TestClient, statuscode: int, object):
    res = client.get("/dept/")

    assert res.status_code == statuscode
    assert Counter(res.json()) == Counter(object)


@pytest.mark.parametrize(
    ["deptcode", "statuscode", "object"],
    [("XX", 204, None), ("CS", 409, {"detail": "Exists Already"})],
)
def test_api_post_dept(client: TestClient, deptcode: str, statuscode: int, object):
    iptobj = DepartmentReport(Code=deptcode, Name="X")

    res = client.post("/dept/", json=iptobj.dict())

    assert res.status_code == statuscode
    assert res.json() == object


@pytest.mark.parametrize(
    ["deptcode", "deptcodenew", "statuscode", "object"],
    [
        ("XX", "XV", 404, {"detail": "No Such Department"}),
        ("CS", "XV", 204, None),
        ("CS", "TE", 409, {"detail": "Dept with TE Exists"}),
    ],
)
def test_api_put_dept(
    client: TestClient, deptcode: str, deptcodenew: str, statuscode: int, object
):
    iptobj = DepartmentReport(Code=deptcodenew, Name="X")

    res = client.put("/dept/{}".format(deptcode), json=iptobj.dict())

    assert res.status_code == statuscode
    assert res.json() == object
