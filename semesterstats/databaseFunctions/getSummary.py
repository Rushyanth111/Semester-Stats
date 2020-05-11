from ..Models import BatchSchemeInfo, SubjectDetails, SubjectScore, StudentDetails

from ..Plugins import ProcessMarks, TotalProcessMarks

from .getList import getList

import re


def SortSubject(SubjectScoreObject):
    Matches = re.search(
        "[0-9]{2}([A-Za-z]{2,3})([0-9]{2,3})", SubjectScoreObject["SubjectCode"]
    )
    if Matches.group(1)[-1] == "L" and len(Matches.group(1)) == 3:
        return 1000 + int(Matches.group(2))
    return int(Matches.group(2))


def getSummary(Batch: int, Semester: int, Department: str) -> tuple:
    # Obtain the Summary of the given Batch In JSON format.

    # Fetch the Scheme of the Batch

    Scheme = int(BatchSchemeInfo.get(BatchSchemeInfo.Batch == Batch).Scheme)

    # Get all of the Subject Codes For the Batch, Scheme and Semester.

    SubjectCodes = [
        x.SubjectCode
        for x in SubjectDetails.select(SubjectDetails.SubjectCode).where(
            (SubjectDetails.SubjectSemester == Semester)
            & (SubjectDetails.SubjectScheme == Scheme)
        )
    ]
    # For Each Subject get the following:
    # NO of Students, No of Fail, FCD, FC, SC and Pass Percentage.

    # Get Attendees First

    SerialNumbers = StudentDetails.select(StudentDetails.SerialNumber).where(
        StudentDetails.Batch == Batch
    )
    TotalAttendees = SerialNumbers.count()
    SerialNumbers = [x.SerialNumber for x in SerialNumbers]

    EachDetail = []

    for Code in SubjectCodes:
        CurrentCodeScores = SubjectScore.select(
            SubjectScore.Internals, SubjectScore.Externals
        ).where(
            (SubjectScore.SubjectCode == Code)
            & (SubjectScore.SerialNumber.in_(SerialNumbers))
        )

        SubjectAttendees = CurrentCodeScores.count()
        SubjectTotalPass = 0
        SubjectFCD = 0
        SubjectSC = 0
        SubjectFC = 0
        for Score in CurrentCodeScores:
            IsPass, TotalScore, PassClass = ProcessMarks(
                Scheme, Score.Internals, Score.Externals
            )

            if IsPass is True:
                SubjectTotalPass += 1
            if PassClass == "FCD":
                SubjectFCD += 1
            elif PassClass == "SC":
                SubjectSC += 1
            elif PassClass == "FC":
                SubjectFC += 1
            else:
                continue

        SubjectSummary = {
            "SubjectCode": Code,
            "FacultyName": "N/A",
            "Attendees": SubjectAttendees,
            "Failures": SubjectAttendees - SubjectTotalPass,
            "FCD": SubjectFCD,
            "FC": SubjectFC,
            "SC": SubjectSC,
            "PassPercentage": "{:.2f}%".format(
                (SubjectTotalPass / SubjectAttendees) * 100
            ),
        }
        EachDetail.append(SubjectSummary)

    # Sort the Each Detail
    EachDetail.sort(key=SortSubject)

    # Compute Total Section Via getList <- Not Efficient

    ResTotalList = getList(Batch, Semester, Department)

    TotalPass = 0
    TotalFCD = 0
    TotalSC = 0
    TotalFC = 0
    for x in ResTotalList:
        IsPass, PassClass = TotalProcessMarks(Scheme, x["Overall"]["Total"])

        if IsPass is True:
            TotalPass += 1
        if PassClass == "FCD":
            TotalFCD += 1
        elif PassClass == "SC":
            TotalSC += 1
        elif PassClass == "FC":
            TotalFC += 1
        else:
            continue

    return {
        "TotalAttendees": TotalAttendees,
        "FCD": TotalFCD,
        "FC": TotalFC,
        "SC": TotalSC,
        "Pass": TotalPass,
        "Failures": TotalAttendees - TotalPass,
        "PassPercentage": "{:.2f}%".format((TotalPass / TotalAttendees) * 100),
        "EachSubjectDetail": EachDetail,
    }
