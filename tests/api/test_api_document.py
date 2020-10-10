import pytest
from fastapi.testclient import TestClient


@pytest.mark.parametrize(
    ["batch", "dept", "sem", "rescode"],
    [
        (2014, "CS", 5, 404),
        (2015, "XS", 5, 404),
        (2015, "CS", 6, 200),
    ],
)
def test_get_document(
    client: TestClient, batch: int, dept: str, sem: int, rescode: int
):
    res = client.get("/docs/{}/{}/{}/docx".format(batch, dept, sem))
    assert res.status_code == rescode
