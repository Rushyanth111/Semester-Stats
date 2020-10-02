from typing import List

from sqlalchemy import tuple_
from sqlalchemy.orm import Session

from ..common.reports import DepartmentReport, ScoreReport, StudentReport, SubjectReport
from ..database.models import Department, Score, Student, Subject


def put_department_bulk(db: Session, dept_list: List[DepartmentReport]):
    # Obtain the Departments that are already Present.
    in_dept_codes = set(dept_list)

    db_dept_codes = set(
        [
            DepartmentReport.from_orm(dept)
            for dept in db.query(Department).filter(
                Department.Code.in_([x.Code for x in in_dept_codes])
            )
        ]
    )

    # Obtain the ones that are new.
    not_present = in_dept_codes - db_dept_codes

    # Insert The ones not Present.
    db.bulk_insert_mappings(
        Department, [obj.dict(exclude={"Subjects", "Students"}) for obj in not_present]
    )
    db.commit()


def put_student_bulk(db: Session, student_list: List[StudentReport]):
    in_students = set(student_list)

    db_students = set(
        [
            StudentReport.from_orm(student)
            for student in db.query(Student).filter(
                Student.Usn.in_([x.Usn for x in in_students])
            )
        ]
    )

    not_present = in_students - db_students
    db.bulk_insert_mappings(
        Student, [obj.dict(exclude={"Scores"}) for obj in not_present]
    )
    db.commit()


def put_subject_bulk(db: Session, subject_list: List[SubjectReport]):
    in_subject = set(subject_list)

    db_subjects = set(
        [
            SubjectReport.from_orm(sub)
            for sub in db.query(Subject).filter(
                Subject.Code.in_([x.Code for x in in_subject])
            )
        ]
    )

    not_present = in_subject - db_subjects
    db.bulk_insert_mappings(Subject, [obj.dict() for obj in not_present])
    db.commit()


def put_score_bulk(db: Session, score_list: List[ScoreReport]):
    in_scores = set(score_list)
    in_scores_comb = [(x.Usn, x.SubjectCode) for x in in_scores]

    db_scores = set(
        [
            ScoreReport.from_orm(score)
            for score in db.query(Score).filter(
                tuple_(Score.Usn, Score.SubjectCode).in_(in_scores_comb)
            )
        ]
    )

    # Get Only the new scores.
    not_present = in_scores - db_scores
    db.bulk_insert_mappings(Score, [obj.dict() for obj in not_present])

    # Updating Section.

    # Check if Need To Insert.
    for pi in in_scores:
        for pb in db_scores:
            if pi == pb and pi > pb:
                db.query(Score).filter(
                    Score.Usn == pi.Usn, Score.SubjectCode == pi.SubjectCode
                ).update(
                    {Score.Internals: pi.Internals, Score.Externals: pi.Externals},
                    synchronize_session="fetch",
                )

    db.commit()
