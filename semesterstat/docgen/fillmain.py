from sqlalchemy.orm import Session
from .mainqueries import MainFill

__main_dict = {
    "Batch": "",
    "Semester": "",
    "Department": "",
    "Total": "",
    "FCD": "",
    "FC": "",
    "SC": "",
    "Pass": "",
    "Fail": "",
    "PassP": "",
    "BYear": "",
    "ODEV": "",
}


def __fill_main(db: Session, batch: int, dept: str, sem: int):
    data = MainFill(db, batch, dept, sem)

    res = __main_dict.copy()

    byear = batch + (sem // 2)
    byear = "{}-{}".format(byear, byear + 1)
    odev = "Odd" if bool(sem % 2) else "Even"

    res["Batch"] = str(batch)
    res["Semester"] = str(sem)
    res["Department"] = str(dept)
    res["Total"] = str(data.get_appeared())
    res["FCD"] = str(data.get_fcd())
    res["FC"] = str(data.get_fc())
    res["SC"] = str(data.get_sc())
    res["Pass"] = str(data.get_pass())
    res["Fail"] = str(data.get_fail())
    res["PassP"] = str(data.get_pass_percent())
    res["BYear"] = byear
    res["ODEV"] = odev

    return res
