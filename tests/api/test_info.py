import pytest
from fastapi.testclient import TestClient


@pytest.mark.parametrize(["batch", "op", "rescode"], [(2015, 2015, 200)])
def test_info_route(client: TestClient, batch: int, op: int, rescode: int):
    res = client.get("/info/scheme/{}".format(batch))
    assert res.status_code == rescode
    assert res.json() == op
