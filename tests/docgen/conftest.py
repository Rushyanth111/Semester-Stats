import json
import os

import pytest
from sqlalchemy.orm import Session

from semesterstat.database import Score, Student, Subject
from semesterstat.reports import ScoreReport, StudentReport, SubjectReport


@pytest.fixture(scope="package", autouse=True)
def input_data1(rootdir, engine):
    # Batches: 2015 - CS
    # Semester: 1

    with open(os.path.join(rootdir, "tests/data/data.json")) as f:
        obj = json.load(f)

    db = Session(bind=engine)

    stu_list = [StudentReport(Name="X", Usn=usn).dict() for (usn) in obj["usn"]]
    sub_list = [
        SubjectReport(
            Name="X", Code=code, MinExt=21, MinTotal=40, MaxTotal=100, Credits=4
        ).dict()
        for (code) in obj["subcode"]
    ]
    sco_list = [
        ScoreReport(Usn=usn, SubjectCode=subcode, Internals=inte, Externals=exte).dict()
        for (usn, subcode, inte, exte, _) in obj["scores"]
    ]

    db.bulk_insert_mappings(Student, stu_list)
    db.bulk_insert_mappings(Subject, sub_list)
    db.bulk_insert_mappings(Score, sco_list)
    db.commit()

    db.close()


@pytest.fixture(scope="package", autouse=True)
def input_data2(engine):
    # Batches: 2015 - CS
    # Semester: 1
    pass
