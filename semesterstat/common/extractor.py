import re

# Format of the USN: (Uni Code{3})(Batch{2})(Dept{2})(RollNo{3})
def batch_from_usn(usn: str) -> int:
    restr = "[A-Za-z0-9]{3}([0-9]{2})[A-Z]{2}[0-9]{3}"

    res = re.search(restr, usn).group(1)

    # Regex can be None as well, Incase of Misplaced Data.
    if res is None:
        return None
    else:
        return 2000 + int(res)


def dept_from_usn(usn: str) -> str:

    restr = "[A-Za-z0-9]{3}[0-9]{2}([A-Z]{2})[0-9]{3}"

    res = re.search(restr, usn).group(1)

    if res is None:
        return None
    else:
        return res


def is_diploma(usn: str) -> bool:
    restr = "[A-Za-z0-9]{3}[0-9]{2}[A-Z]{2}([0-9]{3})"

    res = re.search(restr, usn).group(1)

    if res is None:
        return None
    else:
        return True if int(res) >= 400 else False


# Format of SubjetCode: (Scheme)(Dept/SubjectCode)(Semester,SubjectNumber)
def semester_from_subject(subcode: str) -> int:
    restr = "[0-9]{2}[A-Z]{2,6}([0-9]{2,3})"

    res = re.search(restr, subcode).group(1)

    if res is None:
        return None
    else:
        return int(res)[0]


def scheme_from_subject(subcode: str) -> int:
    restr = "([0-9]{2})[A-Z]{2,6}[0-9]{2,3}"

    res = re.search(restr, subcode).group(1)

    if res is None:
        return None
    else:
        return 2000 + int(res)


def dept_from_subject(subcode: str) -> str:
    restr = "[0-9]{2}([A-Z]{2,6})[0-9]{2,3}"

    res = re.search(restr, subcode).group(1)

    if res is None:
        return None
    else:
        return res

