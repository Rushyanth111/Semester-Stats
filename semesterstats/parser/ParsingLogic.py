import csv
import re

from peewee import chunked

from ..logging import AppLog
from ..models import (
    BacklogSubjectScore,
    BatchSchemeInfo,
    ParsedTable,
    StudentDetails,
    SubjectDetails,
    SubjectScore,
    db,
)
from .Utils import (
    get_serial_number_department,
    get_subject_department,
    get_subject_semester,
)


def parse_into_database(filename: str) -> None:
    ParsedFilename = re.search(
        "Data-([A-Za-z]*)-([0-9]*)-([0-9]*)-([0-9]*)(-[Aa]rrear)?.csv", filename
    )
    Department = ParsedFilename.group(1).upper()
    Batch = int(ParsedFilename.group(2))
    Scheme = int(ParsedFilename.group(3))
    Semester = int(ParsedFilename.group(4))
    Arrear = False if ParsedFilename.group(5) is None else True

    # Weird Check LOL
    if not Scheme <= Batch:
        AppLog.info(f"{filename} contains Invalid Details")
        return
    # Check if the particular Batch exists?
    record, created = BatchSchemeInfo.get_or_create(Batch=Batch, Scheme=Scheme)

    if created is True:
        AppLog.info(f"{Batch}-{Scheme} Added to BatchSchemeInfo")

    # Check if the particular File has been Parsed:
    record, created = ParsedTable.get_or_create(
        Batch=Batch, Department=Department, Semester=Semester, Arrear=Arrear
    )

    if created is False:
        AppLog.info(f"{filename} has already been Parsed, Skipping...")
        return
    else:
        AppLog.info(f"{filename} is being Parsed...")

    Year = Batch + (Semester // 2)
    YearIndicator = (bool(Semester % 2 == 0),)

    with open(filename) as file:
        reader = csv.reader(file, delimiter=",", skipinitialspace=True)

        # Set of Keys that Exists

        # Set The existing ones

        StudentDetailsArrayExists = StudentDetails.select(
            StudentDetails.SerialNumber
        ).tuples()
        SubjectDetailsArrayExists = SubjectDetails.select(
            SubjectDetails.SubjectCode
        ).tuples()
        ScoreDetailsArrayExists = (
            SubjectScore.select(SubjectScore.SerialNumber, SubjectScore.SubjectCode)
            .distinct()
            .tuples()
        )

        StudentDetailsArray = set()
        SubjectDetailsArray = set()
        ScoreDetailsArray = set()

        for row in reader:
            SerialNumber = str(row[0]).upper()
            Name = row[1]
            Department = get_serial_number_department(SerialNumber)
            # Scheme Defined Above.

            if (SerialNumber,) not in StudentDetailsArrayExists:
                StudentDetailsArray.add((SerialNumber, Name, Batch, Department))

            for itr in range(3, len(row[3:]), 6):
                # Looping Within the Array
                SubjectCode = row[itr]
                SubjectName = row[itr + 1]
                SubjectSemester = get_subject_semester(SubjectCode)
                SubjectDepartment = get_subject_department(SubjectCode)
                Internal = row[itr + 2]
                External = row[itr + 3]

                if (SubjectCode,) not in SubjectDetailsArrayExists:
                    SubjectDetailsArray.add(
                        (
                            SubjectCode,
                            SubjectName,
                            SubjectSemester,
                            Scheme,
                            SubjectDepartment,
                        )
                    )

                if (SerialNumber, SubjectCode,) in ScoreDetailsArrayExists:
                    AppLog.info(
                        f"Moving Backlog {SerialNumber}-{SubjectCode} Score to Backlog Table...",
                    )
                    query = SubjectScore.get(
                        (SubjectScore.SerialNumber == SerialNumber)
                        & (SubjectScore.SubjectCode == SubjectCode)
                    )
                    BacklogSubjectScore.insert_from(
                        query,
                        fields=[
                            BacklogSubjectScore.SerialNumber,
                            BacklogSubjectScore.SubjectCode,
                            BacklogSubjectScore.Year,
                            BacklogSubjectScore.YearIndicator,
                            BacklogSubjectScore.Internals,
                            BacklogSubjectScore.Externals,
                        ],
                    )
                    query.delete_instance()

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
                        StudentDetails.Batch,
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
                        SubjectDetails.SubjectScheme,
                        SubjectDetails.SubjectDepartment,
                    ],
                ).on_conflict_ignore().execute()

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