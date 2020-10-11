import re


# Format of the USN: (Uni Code{3})(Batch{2})(Dept{2})(RollNo{3})
def get_usn_batch(usn: str) -> int:
    restr = "[A-Za-z0-9]{3}([0-9]{2})[A-Z]{2}([0-9]{3})"

    reg = re.search(restr, usn)
    res = reg.group(1)
    dip = reg.group(2)

    # Regex can be None as well, Incase of Misplaced Data.
    if res is None or dip is None:
        return None
    else:
        if int(dip) >= 400:
            return 2000 + int(res) - 1
        else:
            return 2000 + int(res)


def get_usn_dept(usn: str) -> str:

    restr = "[A-Za-z0-9]{3}[0-9]{2}([A-Z]{2})[0-9]{3}"

    res = re.search(restr, usn).group(1)

    if res is None:
        return None
    else:
        return res


def is_usn_diploma(usn: str) -> bool:
    restr = "[A-Za-z0-9]{3}[0-9]{2}[A-Z]{2}([0-9]{3})"

    res = re.search(restr, usn).group(1)

    if res is None:
        return None
    else:
        return True if int(res) >= 400 else False
