from semesterstat.crud.subject import get_subject, is_subject_exist
from semesterstat.crud.student import get_student, is_student_exists
from semesterstat.crud.bulk import put_student_bulk, put_subject_bulk
from semesterstat.common.reports import (
    DepartmentReport,
    ScoreReport,
    StudentReport,
    SubjectReport,
)
from semesterstat.crud import (
    put_score_bulk,
    get_student_subject,
    put_department_bulk,
    is_dept_exist,
    get_dept_by_code,
)
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


def test_put_department_bulk(db: Session):
    ins_list = [
        DepartmentReport(Code=code, Name=name)
        for (code, name) in [
            ("XE", "Some Random Department"),
            ("CS", "BadString"),  # This should be Ignored.
        ]
    ]

    put_department_bulk(db, ins_list)
    assert is_dept_exist(db, "XE")

    res = get_dept_by_code(db, "CS")

    assert res.Name == "Computer Science"

    db.rollback()


def test_put_student_bulk(db: Session):
    ins_list = [
        StudentReport(Usn=usn, Name=name)
        for (usn, name) in [
            ("1CR15CS001", "X"),
            ("1CR15CS002", "X2"),
            ("1CR15CS101", "X3"),
        ]
    ]

    put_student_bulk(db, ins_list)
    assert is_student_exists(db, "1CR15CS001")
    assert is_student_exists(db, "1CR15CS002")

    res = get_student(db, "1CR15CS101")
    # No Change from Conftest
    assert res.Name == "X"

    db.rollback()


def test_put_subject_bulk(db: Session):
    ins_list = [
        SubjectReport(Code=code, Name=name)
        for (code, name) in [
            ("15CS81", "X"),
            ("15CS64", "X3"),
        ]  # Last Shouldn't Shouldn't change
    ]

    put_subject_bulk(db, ins_list)

    assert is_subject_exist(db, "15CS81")

    res = get_subject(db, "15CS64")

    assert res.Name == "X"

    db.rollback()
