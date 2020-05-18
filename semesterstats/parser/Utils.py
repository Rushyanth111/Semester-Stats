import re


# Gets The Semester Based on the Given Subject Code.
def get_subject_semester(string: str):
    Matches = re.search("[0-9]{2}[A-Z]{2,4}([0-9]{2,3})", string)
    return int(Matches.group(1)[0])


# Gets the Department Based on the Given USN
def get_serial_number_department(string: str):
    Matches = re.search("1CR[0-9]{2}([A-Z]{2})[0-9]{3}", string)
    return Matches.group(1)


def get_subject_department(string: str) -> str:
    pass
    # Matches = re.search("[0-9]{2}([A-Z]{2,4})[0-9]{2,3}", string)
    # Department: str = Matches.group(1)
    # # Special Processing for Labs in Particular.
    # # Labs always End with L and are three characters Long.
    # if (
    #     Department[-1] == "L"
    #     and Department[0 : len(Department)] in DepartmentCodeDictionary
    # ):
    #     return Department[0:2].upper()
    # elif Department in DepartmentCodeDictionary:
    #     return Department
    # else:
    #     return "XTR"
