import csv
import re



# CSV Format
"""
USN, Name, Attempted Subjects, [SubCode, Subname,Internals,Externals,Total,Fail/Pass]xAttemptedSubjects
"""


def getSemester(string: str):
    matches = re.search("[0-9]{2}[A-Z]{2,3}([0-9]{2,3})", string)
    return int(matches.group(1)[0])


filename = "imported/6th_sem_cse.csv"
year = 2018
even = True


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
            [StudentDetails.SerialNumber, StudentDetails.Name, StudentDetails.Scheme],
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
