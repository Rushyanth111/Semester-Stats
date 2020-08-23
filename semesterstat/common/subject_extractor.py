import re

from ..constants.dept import dept_dict

# Format of SubjetCode: (Scheme)(Dept/SubjectCode)(Semester,SubjectNumber)


def get_subject_semester(subcode: str) -> int:
    restr = "[0-9]{2}[A-Z]{2,6}([0-9]{2,3})"

    res = re.search(restr, subcode).group(1)

    if res is None:
        return None
    else:
        return int(res[0])


def get_subject_scheme(subcode: str) -> int:
    restr = "([0-9]{2})[A-Z]{2,6}[0-9]{2,3}"

    res = re.search(restr, subcode).group(1)

    if res is None:
        return None
    else:
        return 2000 + int(res)


def get_subject_dept(subcode: str) -> str:
    restr = "[0-9]{2}([A-Z]{2,6})[0-9]{2,3}"

    res = re.search(restr, subcode).group(1)

    if res is None:
        return None

    # Department Can be two or Three Characters Long, Check for Length

    if len(res) == 2 and res in dept_dict:
        # If Two, then just check in dept list
        return res

    if len(res) == 3:
        # If Three, then Check if the Last ends with S or L.
        # If True, then Check in dept_dict if remaining string exist.
        # Else, check in dept_dict if exists, else, return BS

        if res[-1] in ("L", "S") and res[: len(res) - 1] in dept_dict:
            return res[: len(res) - 1]

        elif res in dept_dict:
            return res

    if len(res) == 4 and res[-2:] == "MP" and res[: len(res) - 2] in dept_dict:
        # Check for MP At the end, if so, check for
        return res[: len(res) - 2]

    # If all Else Fails, Return XX -> Basic Science

    return "XX"


def is_subject_lab(subcode: str) -> bool:
    restr = "[0-9]{2}([A-Z]{2,6})[0-9]{2,3}"

    res = re.search(restr, subcode).group(1)

    if res is None:
        return None
    else:
        return True if res[-1] == "L" else False
