from mailmerge import MailMerge
from ..config import db


def docs_mail_merge_gen(batch: int, semester: int, department: str):
    Data = db.external_get_batch_semester_summary(batch, department, semester)

    with MailMerge("Resources/TemplateDocument.docx") as document:
        MainInformation = {
            "Total": str(Data["TotalAttendees"]),
            "FCD": str(Data["FCD"]),
            "FC": str(Data["FC"]),
            "SC": str(Data["SC"]),
            "Pass": str(Data["Pass"]),
            "Fail": str(Data["Fail"]),
            "PassP": "{:.2f}".format(Data["PassPercentage"]),
            "Batch": str(batch),
            "ODEV": "Odd",
            "BYear": "2019",
            "Department": str(db.external_get_department(department).DepartmentName),
            "Semester": str(semester),
            "DPS": str(department),
        }

        rows = []
        row_f = []
        for subject in Data["SubjectCodes"]:
            d = {
                "SubjectCodeT": str(subject),
                "TeachersNameT": str("Placeholder for long string here"),
                "AppT": str(Data[subject]["TotalAttendees"]),
                "FailT": str(Data[subject]["Fail"]),
                "R1": str(Data[subject]["FCD"]),
                "R2": str(Data[subject]["FC"]),
                "R3": str(Data[subject]["SC"]),
                "PPT": "{:.2f}".format(Data[subject]["PassPercentage"]) + "%",
            }
            rows.append(d)
        d = {}
        for x in list(rows[-1].keys()):
            d[x + "F"] = rows[-1][x]
        row_f.append(d)

        rows = rows[: len(rows) - 1]

        document.merge(**MainInformation)
        document.merge_rows("SubjectCodeT", rows)

        document.merge_rows("SubjectCodeTF", row_f)
        document.write("demo.docx")
