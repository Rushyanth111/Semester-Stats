from sqlalchemy import func
from sqlalchemy.orm import Session

from semesterstat.database.models import Score, Student, Subject

from ...reciepts import BatchScoreSumReciept, BatchScoreSumList


def get_batch_scores_sum(
    db: Session, batch: int, dept: str = None
) -> BatchScoreSumReciept:
    """Obtain the Batch CGPA of all USNs in that batch.

    Args:
        db (Session): SQLAlchemy Session
        batch (int): Batch for which to obtain results.
        dept (str, optional): [description]. Department Filter.

    Raises:
        NoResultFound

    Returns:
        -
    """
    score_list = (
        db.query(
            Score.Usn, Subject.Semester, func.sum(Score.Internals + Score.Externals)
        )
        .join(Subject)
        .join(Student)
        .filter(Student.Batch == batch)
        .group_by(Score.Usn, Subject.Semester)
    )

    if dept is not None:
        score_list = score_list.filter(Student.Department == dept)

    # Manual format to a Dict with Usn.

    usn_list = {}

    for (student, semester, scoresum) in score_list:
        # Student, Semester, Sum should be the order.

        if student not in usn_list:
            usn_list[student] = {}

        usn_list[student][semester] = scoresum

    reciept_list = []
    mean = 0

    for (usn, scoresum) in usn_list.items():
        total = sum(list(scoresum.values()))
        avg = total / len(scoresum)
        mean += avg
        temp_container = BatchScoreSumList(
            Usn=usn, ScoreSum=scoresum, Average=avg, Total=total
        )
        reciept_list.append(temp_container)

    mean = mean / len(usn_list) if len(usn_list) > 0 else 0

    res = BatchScoreSumReciept(Mean=mean, ScoreDetail=reciept_list)

    return res
