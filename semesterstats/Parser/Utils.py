import re
from ..Models import DepartmentCodeDictionary


# Gets The Semester Based on the Given Subject Code.
def getSubjectSemester(string: str):
    Matches = re.search("[0-9]{2}[A-Z]{2,3}([0-9]{2,3})", string)
    return int(Matches.group(1)[0])


# Gets the Department Based on the Given USN
def getSerialNumberDepartment(string: str):
    Matches = re.search("1CR[0-9]{2}([A-Z]{2})[0-9]{3}", string)
    return Matches.group(1)


def getSubjectDepartment(string: str) -> str:
    Matches = re.search("[0-9]{2}([A-Z]{2,3})[0-9]{2,3}", string)
    Department: str = Matches.group(1)
    # Special Processing for Labs in Particular.
    # Labs always End with L and are three characters Long.
    if (
        Department[-1] == "L"
        and Department[0 : len(Department)] in DepartmentCodeDictionary
    ):
        return Department[0:2].upper()
    elif Department in DepartmentCodeDictionary:
        return Department
    else:
        return "XTR"


"""
Logical Parsing for Departments:
Let X = Department

if Semester 1 or 2 -> Send to Basic_Science.
elif Semester 3 to 8 ->
    if SerialNumberDepartment for Department Exists ->
        Return Department
    else
        Return Basic
"""
