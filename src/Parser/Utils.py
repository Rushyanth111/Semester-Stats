import re


def getSemester(string: str):
    matches = re.search("[0-9]{2}[A-Z]{2,3}([0-9]{2,3})", string)
    return int(matches.group(1)[0])
