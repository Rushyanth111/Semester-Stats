import pytest
from fastapi.testclient import TestClient
from jsonschema import validate

from semesterstat.reciepts import StudentScoreReciept


def test_batch_get_all(client: TestClient):
    res = client.get("/batch/")
    data = res.json()

    assert res.status_code == 200
    assert isinstance(data, list)
    assert all(isinstance(item, int) for item in data)


@pytest.mark.parametrize(
    ["batch", "dept", "sem", "rescode"],
    [
        (2015, None, None, 200),
        (2015, "CS", None, 200),
        (2015, None, 5, 200),
        (2015, "CS", 6, 200),
        (2014, None, None, 404),
        (2015, "XX", None, 200),
        (2015, None, 6, 200),
    ],
)
def test_batch_get_scores(
    client: TestClient, batch: int, dept: str, sem: int, rescode: int
):
    res = client.get(
        "/batch/{}/scores".format(batch),
        params={"dept": dept, "sem": sem},
    )

    assert res.status_code == rescode
    data = res.json()

    if rescode == 200:
        # Check if Instance of List[StudentScoreReciept]
        for item in data:
            validate(item, StudentScoreReciept.schema())

    elif rescode == 404:
        assert data == {"detail": "Batch Does Not Exist"}


@pytest.mark.parametrize(
    ["batch", "dept", "thresh", "rescode"],
    [
        (2015, "CS", 1, 200),
        (2015, "CS", 2, 200),
        (2015, "TE", 1, 200),
        (2015, "TE", 3, 200),
        (2014, "CS", 1, 404),
    ],
)
def test_batch_detained(
    client: TestClient, batch: int, dept: str, thresh: int, rescode: int
):
    res = client.get(
        "/batch/{}/detained".format(batch), params={"dept": dept, "thresh": thresh}
    )

    assert res.status_code == rescode
    data = res.json()

    if rescode == 200:
        for item in data:
            validate(item, StudentScoreReciept.schema())
    elif rescode == 404:
        assert data == {"detail": "Batch Does Not Exist"}


@pytest.mark.parametrize(
    ["batch", "dept", "sem", "rescode"],
    [
        (2015, "CS", 6, 200),
        (2015, "CS", 5, 200),
        (2014, "CS", 1, 404),
    ],
)
def test_batch_backlogs(
    client: TestClient, batch: int, dept: str, sem: int, rescode: int
):
    res = client.get(
        "/batch/{}/backlogs".format(batch), params={"dept": dept, "sem": sem}
    )

    assert res.status_code == rescode
    data = res.json()

    if rescode == 200:
        for item in data:
            validate(item, StudentScoreReciept.schema())
    elif rescode == 404:
        assert data == {"detail": "Batch Does Not Exist"}
