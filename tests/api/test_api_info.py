import pytest
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    ["batch", "rescode"],
    [(2015, 200), (2014, 404)],
)
def test_info_route(client: TestClient, batch: int, rescode: int):
    res = client.get("/info/scheme/{}".format(batch))
    assert res.status_code == rescode
    data = res.json()
    if rescode == 200:
        assert isinstance(data, int)
    elif rescode == 404:
        assert data == {"detail": "Batch Does Not Exist"}
