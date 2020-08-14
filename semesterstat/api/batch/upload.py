from fastapi import APIRouter
from ..common.reports import BulkReport
from ...database import Department, Subject, Student, Score, db

upload = APIRouter()


@upload.post("/", status_code=201)
def parse_batch_results(bulk_reports: BulkReport):
    students = []
    departments = []
    subjects = []
    scores = []
    # Split Each of the Report into the 4 main Categories.
    for report in bulk_reports.report:
        students.append(report.export_student().dict())
        departments.append(report.export_department().dict())
        scores.append(report.export_score().dict())
        subjects.append(report.export_subject().dict())

    # Add them into the database
    # In the Order of:
    # Dept, Subject, Student, Score

    with db.atomic():
        Department.insert_many(departments).execute()

        Subject.insert_many(subjects).on_conflict_ignore().execute()

        Student.insert_many(students).execute()

        Score.insert_many(scores).execute()

    # If Done without error, return a 200.
    return
