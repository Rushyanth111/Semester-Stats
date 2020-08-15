import re


def batch_from_usn(usn: str) -> int:
    # Format of the USN: (Uni Code{3})(Batch{2})(Dept{2})(RollNo{3})
    restr = "[A-Za-z0-9]{3}([0-9]{2})[A-Z]{2}[0-9]{3}"

    res = re.search(restr, usn).group(1)

    # Regex can be None as well, Incase of Misplaced Data.
    if res is None:
        return None
    else:
        return 2000 + int(res)


def dept_from_usn(usn: str) -> str:
    # Format of the USN: (Uni Code{3})(Batch{2})(Dept{2})(RollNo{3})
    restr = "[A-Za-z0-9]{3}[0-9]{2}([A-Z]{2})[0-9]{3}"

    res = re.search(restr, usn).group(1)

    # Regex can be None as well, Incase of Misplaced Data.
    if res is None:
        return None
    else:
        return res


# Format of SubjetCode: (Scheme)(Dept/SubjectCode)(Semester,SubjectNumber)
def semester_from_subject(subcode: str) -> int:
    pass


def scheme_from_subject(subcode: str) -> int:
    pass


def dept_from_subject(subcode: str) -> str:
    pass
