import pytest
from sqlalchemy.orm import Session

from semesterstat.database import Score, Student, Subject
from semesterstat.reports import ScoreReport, StudentReport, SubjectReport


@pytest.fixture(scope="package", autouse=True)
def input_data(engine):

    db = Session(bind=engine)

    stu_data = [
        StudentReport(Usn=usn, Name=name)
        for (usn, name) in [
            ("1CR15CS101", "X"),
            ("1CR15CS102", "X"),
            ("1CR17TE102", "X"),
            ("1CR17CS102", "X"),
        ]
    ]
    student = [x.dict() for x in stu_data]
    db.bulk_insert_mappings(Student, student)

    subect_data = [
        SubjectReport(
            Code=code, Name=name, MinExt=minext, MinTotal=mintotal, Credits=credits
        )
        for (code, name, minext, mintotal, credits) in [
            ("15CS65", "X", 21, 35, 4),
            ("15CS64", "X", 21, 35, 4),
            ("15CS54", "X", 21, 35, 4),
            ("17MAT11", "X", 21, 35, 4),
            ("17CSL76", "X", 21, 35, 2),
            ("17CS55", "X", 21, 35, 4),
        ]
    ]
    subjects = [x.dict() for x in subect_data]
    db.bulk_insert_mappings(Subject, subjects)

    score_data = [
        ScoreReport(
            Usn=usn, SubjectCode=subcode, Internals=internals, Externals=externals
        )
        for (usn, subcode, internals, externals) in [
            ("1CR15CS101", "15CS65", 12, 42),
            ("1CR15CS101", "15CS64", 16, 15),
            ("1CR15CS102", "15CS54", 19, 29),
            ("1CR17TE102", "17MAT11", 19, 55),
            ("1CR17TE102", "17CSL76", 38, 26),
            ("1CR17CS102", "17CS55", 28, 20),
        ]
    ]
    scores = [x.dict() for x in score_data]
    db.bulk_insert_mappings(Score, scores)

    db.commit()
    db.close()
