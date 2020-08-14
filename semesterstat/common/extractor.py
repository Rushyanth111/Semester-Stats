import re


def batch_from_usn(usn: str) -> int:
    # Format of the USN: (Uni Code{3})(Batch{2})(Dept{2})(RollNo{3})
    restr = "[A-Za-z0-9]{3}([0-9]{3})[A-Z]{2}[0-9]{3}"

    res = re.search(restr, usn)

    # Regex can be None as well, Incase of Misplaced Data.
    if res is None:
        return None
    else:
        return int(res)


def dept_from_usn(usn: str) -> str:
    # Format of the USN: (Uni Code{3})(Batch{2})(Dept{2})(RollNo{3})
    restr = "[A-Za-z0-9]{3}[0-9]{3}([A-Z]{2})[0-9]{3}"

    res = re.search(restr, usn)

    # Regex can be None as well, Incase of Misplaced Data.
    if res is None:
        return None
    else:
        return res


def semester_from_subject(subcode: str) -> int:
    pass


def scheme_from_subject(subcode: str) -> int:
    pass


def dept_from_subject(subcode: str) -> str:
    pass
