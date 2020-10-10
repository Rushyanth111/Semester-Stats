import pytest
from fastapi.testclient import TestClient
from jsonschema import validate

from semesterstat.reciepts import SummaryReciept


@pytest.mark.parametrize(
    ["batch", "dept", "sem", "rescode"],
    [
        (2015, "CS", 6, 200),
        (2015, "CS", 5, 200),
        (2014, "CS", 5, 404),
    ],
)
def test_summary(client: TestClient, batch: str, dept: str, sem: str, rescode: int):
    res = client.get("/summary/{}/{}/{}/".format(batch, dept, sem))

    assert res.status_code == rescode
    data = res.json()

    if rescode == 200:
        validate(data, SummaryReciept.schema())
    elif rescode == 404:
        assert (
            data == {"detail": "Batch Does Not Exist"}
            or data == {"detail": "Dept Does Not Exist"}
            or data == {"detail": "No Records Exist"}
        )
