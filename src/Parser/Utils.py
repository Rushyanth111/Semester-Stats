import re

# Gets The Semester Based on the Given Subject Code.
def getSubjectSemester(string: str):
    matches = re.search("[0-9]{2}[A-Z]{2,3}([0-9]{2,3})", string)
    return int(matches.group(1)[0])


# Gets the Department Based on the Given USN
def getSerialNumberDepartment(string: str):
    matches = re.search("1CR[0-9]{2}([A-Z]{2})[0-9]{3}", string)
    return matches.group(1)


def getSubjectDepartment(string: str) -> str:
    matches = re.search("[0-9]{2}([A-Z]{2,3})[0-9]{2,3}", string)
    return matches.group(1)
