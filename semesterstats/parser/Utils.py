import re
from ..config import db


# Gets The Semester Based on the Given Subject Code.
def get_subject_semester(string: str):
    Matches = re.search("[0-9]{2}[A-Z]{2,4}([0-9]{2,3})", string)
    return int(Matches.group(1)[0])


# Gets the Department Based on the Given USN
def get_serial_number_department(string: str):
    Matches = re.search("1CR[0-9]{2}([A-Z]{2})[0-9]{3}", string)
    return Matches.group(1)


# https://github.com/Rushyanth111/Semster-Stats/issues/21
def get_subject_department(string: str) -> str:
    matches = re.search("[0-9]{2,6}([A-Z]{2,})[0-9]{2,3}", string)
    department: str = matches.group(1).upper()

    # Check if it ends with an L, whihch is a laboratory.
    # Check if it ends with an P, which is a Project
    if department[-1] == "L" or department[-1] == "P":
        if db.get_department(department[0 : len(department) - 1]) is not None:
            return db.get_department(department[0 : len(department) - 1]).DepartmentCode
        else:
            return "XTR"
    elif db.get_department(department) is not None:
        return db.get_department(department).DepartmentCode
    else:
        return "XTR"
