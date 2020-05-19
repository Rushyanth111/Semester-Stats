from mailmerge import MailMerge
from ..response_builder import get_summary

DepartmentCodeDictionary = {}


def docsGeneratorAlternate(Batch: int, Semester: int, Department: str):
    Data = get_summary(Batch, Semester, Department)
    with MailMerge("TemplateDocument.docx") as document:
        print(document.get_merge_fields())
        MainInformation = {
            "Total": str(Data["TotalAttendees"]),
            "FCD": str(Data["FCD"]),
            "FC": str(Data["FC"]),
            "SC": str(Data["SC"]),
            "Pass": str(Data["Pass"]),
            "Fail": str(Data["Failures"]),
            "PassP": Data["PassPercentage"],
            "Batch": str(Batch),
            "ODEV": "Odd",
            "BYear": "2019",
            "Department": DepartmentCodeDictionary.get(Department),
            "Semester": str(Semester),
            "DPS": str(Department),
        }

        Rows = []
        RowF = []
        for SubjectDetail in Data["EachSubjectDetail"]:
            d = {
                "SubjectCodeT": SubjectDetail["SubjectCode"],
                "TeachersNameT": SubjectDetail["FacultyName"]
                + str("Placeholder for long string here"),
                "AppT": str(SubjectDetail["Attendees"]),
                "FailT": str(SubjectDetail["Failures"]),
                "R1": str(SubjectDetail["FCD"]),
                "R2": str(SubjectDetail["FC"]),
                "R3": str(SubjectDetail["SC"]),
                "PPT": str(SubjectDetail["PassPercentage"]),
            }
            Rows.append(d)
        d = {}
        for x in list(Rows[-1].keys()):
            d[x + "F"] = Rows[-1][x]
        RowF.append(d)

        Rows = Rows[: len(Rows) - 1]

        document.merge(**MainInformation)
        document.merge_rows("SubjectCodeT", Rows)

        document.merge_rows("SubjectCodeTF", RowF)
        document.write("demo.docx")
