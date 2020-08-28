from semesterstat.common.reports import ScoreReport
from semesterstat.crud import put_score_bulk, get_student_subject
from sqlalchemy.orm import Session


def test_put_score_bulk(db: Session):
    fix = [
        ScoreReport(Usn=usn, SubjectCode=subcode, Internals=inte, Externals=exte)
        for (usn, subcode, inte, exte) in [
            ("1CR15CS101", "15CS61", 12, 34),
            ("1CR15CS101", "15CS62", 12, 34),
            ("1CR15CS101", "15CS63", 12, 34),
            ("1CR15CS101", "15CS64", 30, 50),
        ]
    ]

    put_score_bulk(db, fix)

    res = get_student_subject(db, "1CR15CS101", "15CS61")
    assert res.Internals == 12
    assert res.Externals == 34

    res = get_student_subject(db, "1CR15CS101", "15CS64")
    assert res.Internals == 30
    assert res.Externals == 50

    db.rollback()
