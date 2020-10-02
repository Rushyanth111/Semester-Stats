from sqlalchemy.orm import Session
from .subjectqueries import SubjectFill
from typing import Dict

__subject_dict = {
    "SubjectCodeT": "",
    "TeachersNameT": "",
    "AppT": "",
    "FailT": "",
    "R1": "",
    "R2": "",
    "R3": "",
    "PPT": "",
}


def __fill_subject(db: Session, subcode: str, batch: int, dept: str) -> Dict[str, str]:
    data = SubjectFill(db, subcode, batch, dept)

    res = __subject_dict.copy()

    res["SubjectCodeT"] = subcode
    res["TeachersNameT"] = "Long String as a Placeholder for Future Change"
    res["AppT"] = str(data.get_appeared())
    res["FailT"] = str(data.get_failed())
    res["R1"] = str(data.get_fcd())
    res["R2"] = str(data.get_fc())
    res["R3"] = str(data.get_sc())
    res["PPT"] = str(data.get_pass_percent())

    return res
