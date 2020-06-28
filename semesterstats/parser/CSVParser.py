import csv
import re

from ..logging import AppLog
from ..config import db
from ..models import (
    StudentModel,
    SubjectModel,
    ScoreModel,
)

from .Utils import (
    get_subject_department,
    get_subject_semester,
)


def csv_parser(filename: str) -> None:
    AppLog.info(f"Recieved {filename} for parsing...")
    parsed_filename = re.search(
        "Data-([A-Za-z]*)-([0-9]*)-([0-9]*)-([0-9]*)(-[Aa]rrear)?.csv", filename
    )
    deparment = parsed_filename.group(1).upper()
    batch = int(parsed_filename.group(2))
    scheme = int(parsed_filename.group(3))
    semester = int(parsed_filename.group(4))
    arrear = False if parsed_filename.group(5) is None else True

    if db.get_parsed(deparment, scheme, batch, semester, arrear) is True:
        AppLog.info(
            f"Previously Parsed:{deparment} - {batch} {semester} {arrear}, Skipping..."
        )
        return

    else:
        db.insert_parsed(deparment, scheme, batch, semester, arrear)
        AppLog.info(f"Parsing: {deparment} - {batch} {semester} {arrear}")

    if db.get_scheme(batch) is None and not arrear:
        db.insert_batch_scheme(scheme, batch)
        AppLog.info(f"Added {batch} - {scheme} to existing List.")

    reader = csv.reader(open(filename), delimiter=",", skipinitialspace=True)

    with db.process_bulk() as helper:
        for row in reader:
            student_usn = str(row[0].upper())
            student_name = row[1]
            # Department and scheme defined above.

            helper.insert(
                StudentModel(
                    StudentUSN=student_usn,
                    StudentName=student_name,
                    StudentBatch=batch,
                    StudentDepartment=deparment,
                )
            )

            for itr in range(3, len(row[3:]), 6):
                sub_code = row[itr]
                sub_name = row[itr + 1]
                sub_sem = get_subject_semester(sub_code)
                sub_dept = get_subject_department(sub_code)
                internal = row[itr + 2]
                external = row[itr + 3]

                helper.insert(
                    SubjectModel(
                        SubjectDepartment=sub_dept,
                        SubjectName=sub_name,
                        SubjectSemester=sub_sem,
                        SubjectScheme=scheme,
                        SubjectCode=sub_code,
                    )
                )

                helper.insert(
                    ScoreModel(
                        ScoreSerialNumber=student_usn,
                        ScoreSubjectCode=sub_code,
                        ScoreSemester=semester,
                        ScoreInternals=internal,
                        ScoreExternals=external,
                    )
                )
