import pytest
from sqlalchemy.orm.session import Session
from semesterstat.crud.batch.batch_scoresum import get_batch_scores_sum
from semesterstat.reciepts import BatchScoreSumReciept, BatchScoreSumList


@pytest.mark.parametrize(
    ["batch", "dept", "op"],
    [
        (
            2017,
            "CS",
            BatchScoreSumReciept(
                ScoreDetail=[
                    BatchScoreSumList(
                        Usn="1CR17CS102",
                        ScoreSum={5: 48},
                        Average=48,
                        Total=48,
                        Mean=48,
                    )
                ],
                Mean=48,
            ),
        ),
        (2014, None, BatchScoreSumReciept(Mean=0, ScoreDetail=[])),
    ],
)
def test_batch_score_sum(db: Session, batch: int, dept: str, op: BatchScoreSumReciept):
    res = get_batch_scores_sum(db, batch, dept)

    assert res.Mean == op.Mean
    if res.ScoreDetail:
        assert res.ScoreDetail[0].Usn == op.ScoreDetail[0].Usn
        assert res.ScoreDetail[0].ScoreSum == op.ScoreDetail[0].ScoreSum
        assert res.ScoreDetail[0].Average == op.ScoreDetail[0].Average
        assert res.ScoreDetail[0].Total == op.ScoreDetail[0].Total
