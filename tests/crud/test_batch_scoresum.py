import pytest
from collections import Counter
from sqlalchemy.orm.session import Session
from semesterstat.crud.batch.batch_scoresum import get_batch_scores_sum
from semesterstat.reciepts import BatchScoreSumReciept


@pytest.mark.parametrize(
    ["batch", "dept", "op"],
    [
        (2017, "CS", [BatchScoreSumReciept(Usn="1CR17CS102", ScoreSum={5: 48})]),
        (
            2015,
            "CS",
            [
                BatchScoreSumReciept(Usn="1CR15CS101", ScoreSum={6: 85}),
                BatchScoreSumReciept(Usn="1CR15CS102", ScoreSum={5: 48}),
            ],
        ),
        (2014, None, []),
    ],
)
def test_batch_score_sum(db: Session, batch: int, dept: str, op):
    res = get_batch_scores_sum(db, batch, dept)

    res_usn = [x.Usn for x in res]
    op_usn = [x.Usn for x in op]

    assert Counter(res_usn) == Counter(op_usn)
