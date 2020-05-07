import csv
import re
from timeit import default_timer as timer

from peewee import IntegrityError as Iex, chunked

from models.BasicModels import (
    StudentDetails,
    SubjectDetails,
    SubjectScore,
    db,
    BacklogSubjectScore,
)
from .Utils import getSubjectSemester, getSerialNumberDepartment, getSubjectDepartment


# CSV Format
"""
USN, Name, Attempted Subjects, [SubCode, Subname,Internals,Externals,Total,Fail/Pass]xAttemptedSubjects
"""


def ParseIntoDatabase(filename: str) -> None:

    ParsedFilename = re.search(
        "Data-([0-9]*)-([0-9]*)-([0-9]*)(-[Aa]rrear)?.csv", filename
    )

    Batch = int(ParsedFilename.group(1))
    Scheme = int(ParsedFilename.group(2))
    Semester = int(ParsedFilename.group(3))

    Year = Batch + (Semester // 2)
    YearIndicator = (bool(Semester % 2 == 0),)

    with open(filename) as file:
        reader = csv.reader(file, delimiter=",", skipinitialspace=True)

        StudentDetailsArray = set()
        SubjectDetailsArray = set()
        ScoreDetailsArray = set()

        for row in reader:
            SerialNumber = str(row[0]).upper()
            Name = row[1]
            Department = getSerialNumberDepartment(SerialNumber)
            # Scheme Defined Above.

            query = StudentDetails.select().where(
                StudentDetails.SerialNumber == SerialNumber
            )
            if not query.exists():
                StudentDetailsArray.add((SerialNumber, Name, Scheme, Department))

            for itr in range(3, len(row[3:]), 6):
                # Looping Within the Array
                SubjectCode = row[itr]
                SubjectName = row[itr + 1]
                SubjectSemester = getSubjectSemester(SubjectCode)
                SubjectDepartment = getSubjectDepartment(SubjectCode)
                Internal = row[itr + 2]
                External = row[itr + 3]

                query = SubjectDetails.select().where(
                    SubjectDetails.SubjectCode == SubjectCode
                )
                if not query.exists():
                    SubjectDetailsArray.add(
                        (SubjectCode, SubjectName, SubjectSemester, SubjectDepartment)
                    )

                query = SubjectScore.select().where(
                    (SubjectScore.SerialNumber == SerialNumber)
                    & (SubjectScore.SubjectCode == SubjectCode)
                )
                if query.exists():
                    BacklogSubjectScore.insert_from(
                        SubjectScore.select().where(
                            (SubjectScore.SerialNumber == SerialNumber)
                            & (SubjectScore.SubjectCode == SubjectCode)
                        ),
                        fields=[
                            BacklogSubjectScore.SerialNumber,
                            BacklogSubjectScore.SubjectCode,
                            BacklogSubjectScore.Year,
                            BacklogSubjectScore.YearIndicator,
                            BacklogSubjectScore.Internals,
                            BacklogSubjectScore.Externals,
                        ],
                    )
                    SubjectScore.delete().where(
                        (SubjectScore.SerialNumber == SerialNumber)
                        & (SubjectScore.SubjectCode == SubjectCode)
                    ).execute()

                ScoreDetailsArray.add(
                    (SerialNumber, SubjectCode, Year, YearIndicator, Internal, External)
                )

        with db.atomic():
            for batch in chunked(StudentDetailsArray, 250):
                StudentDetails.insert_many(
                    batch,
                    [
                        StudentDetails.SerialNumber,
                        StudentDetails.Name,
                        StudentDetails.Scheme,
                        StudentDetails.Department,
                    ],
                ).execute()

            for batch in chunked(SubjectDetailsArray, 250):
                SubjectDetails.insert_many(
                    batch,
                    [
                        SubjectDetails.SubjectCode,
                        SubjectDetails.SubjectName,
                        SubjectDetails.SubjectSemester,
                        SubjectDetails.SubjectDepartment,
                    ],
                ).execute()

            for batch in chunked(ScoreDetailsArray, 100):
                SubjectScore.insert_many(
                    batch,
                    [
                        SubjectScore.SerialNumber,
                        SubjectScore.SubjectCode,
                        SubjectScore.Year,
                        SubjectScore.YearIndicator,
                        SubjectScore.Internals,
                        SubjectScore.Externals,
                    ],
                ).execute()
