import csv
from peewee import SqliteDatabase, IntegrityError as Iex
from models.BasicModels import StudentDetails, SubjectDetails, SubjectScore
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
    XXitr = 0
    for row in reader:
        try:
            StudentDetails.create(SerialNumber=row[0], Name=row[1], Scheme=row[2])
        except Iex:
            pass
        row.pop()
        print(row)
        for itr in range(3, len(row[3:]), 6):
            try:
                SubjectDetails.create(
                    SubjectCode=row[itr],
                    SubjectName=row[itr + 1],
                    SubjectSemester=getSemester(row[itr]),
                )
            except Iex:
                pass
            score_details = SubjectScore.create(
                SerialNumber=row[0],
                SubjectCode=row[itr],
                Year=year,
                YearIndicator=even,
                Internals=row[itr + 2],
                Externals=row[itr + 3],
            )

for person in StudentDetails.select():
    print(person.Name)

"""

"""
