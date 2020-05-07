import csv
from timeit import default_timer as timer

from peewee import IntegrityError as Iex

from models.BasicModels import StudentDetails, SubjectDetails, SubjectScore, db


def ParseIntoDatabase(
    filename: string, semester: str, year: str, scheme: str, even: str
) -> None:
    with open(filename) as file:
        reader = csv.reader(file, delimiter=",", skipinitialspace=True)

        StudentDetailsArray = set()
        SubjectDetailsArray = set()
        ScoreDetailsArray = set()

        for row in reader:
            StudentDetailsArray.add((row[0], row[1], 6))

            for itr in range(3, len(row[3:]), 6):
                SubjectDetailsArray.add((row[itr], row[itr + 1], getSemester(row[itr])))
                ScoreDetailsArray.add(
                    (row[0], row[itr], year, even, row[itr + 2], row[itr + 3],)
                )

        with db.atomic():
            StudentDetails.insert_many(
                StudentDetailsArray,
                [
                    StudentDetails.SerialNumber,
                    StudentDetails.Name,
                    StudentDetails.Scheme,
                ],
            ).execute()

            SubjectDetails.insert_many(
                SubjectDetailsArray,
                [
                    SubjectDetails.SubjectCode,
                    SubjectDetails.SubjectName,
                    SubjectDetails.SubjectSemester,
                ],
            ).execute()

            SubjectScore.insert_many(
                ScoreDetailsArray,
                [
                    SubjectScore.SerialNumber,
                    SubjectScore.SubjectCode,
                    SubjectScore.Year,
                    SubjectScore.YearIndicator,
                    SubjectScore.Internals,
                    SubjectScore.Externals,
                ],
            ).execute()
