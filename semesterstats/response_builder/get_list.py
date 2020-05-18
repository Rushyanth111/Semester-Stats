from ..models import SubjectScore, BatchSchemeInfo, SubjectDetails, StudentDetails

from ..scheme import process_marks


def get_list(Batch: int, Semester: int, Deparment: str):
    # Get the Scheme of said batch
    Scheme = BatchSchemeInfo.get(BatchSchemeInfo.Batch == Batch).Scheme

    # Get all of the Subjects in said Scheme and Semester
    SubjectCodes = [
        x.SubjectCode
        for x in SubjectDetails.select(SubjectDetails.SubjectCode).where(
            (SubjectDetails.SubjectSemester == Semester)
            & (SubjectDetails.SubjectScheme == Scheme)
        )
    ]

    # Get all of the Serial Numbers of Batch:
    StudentQuery = StudentDetails.select(
        StudentDetails.Name, StudentDetails.SerialNumber
    ).where(StudentDetails.Batch == Batch)

    ResultArray: list = []

    for Student in StudentQuery:
        Name = Student.Name
        SerialNumber = Student.SerialNumber
        StudentScoreArray = []
        StudentTotalScore = 0
        StudentIsPass = True

        # Get all Scores for the USN.
        Scores = SubjectScore.select(
            SubjectScore.SubjectCode, SubjectScore.Internals, SubjectScore.Externals
        ).where(
            (SubjectScore.SerialNumber == SerialNumber)
            & (SubjectScore.SubjectCode.in_(SubjectCodes))
        )

        if not Scores.exists():
            continue

        # Process the scores.
        for S in Scores:
            IsPass, TotalScore, PassClass = process_marks(
                Scheme, S.Internals, S.Externals
            )
            StudentTotalScore += TotalScore
            StudentIsPass = StudentIsPass and IsPass
            IsPassString = "Pass" if IsPass is True else "False"
            MarkDict = {
                "Code": str(S.SubjectCode),
                "Internal": S.Internals,
                "External": S.Externals,
                "Total": TotalScore,
                "Result": IsPassString,
                "Class": PassClass,
            }
            StudentScoreArray.append(MarkDict)

        StudentIsPassString = "Pass" if StudentIsPass is True else "False"
        Overall = {"Total": StudentTotalScore, "Result": StudentIsPassString}

        StudentResult = {
            "Name": Name,
            "USN": SerialNumber,
            "Section": "NA",
            "Marks": StudentScoreArray,
            "Overall": Overall,
        }

        ResultArray.append(StudentResult)

    return ResultArray
