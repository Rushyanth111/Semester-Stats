"""
Mail Merge Variables:
The Below Variables are in the format:

Feild: Desc, Full/Short, Type, Example


Global
---------------------------------------------------
Batch: Batch, Short, Str, 2017
Semester: Semester, Full, Int, 6
Department: Department, Full, Str, Computer Science and Engineering.


Total Appeared: Number of Total Appeared in all Examinations, Full, Int, 200
FCD: Number Total of FCDs, Full, Int, 90
FC: Number Total of FCs, Full, Int, 50
SC: Number Total of SCs, Full, Int, 20
Pass: Number Total of Pass, Full, Int, 160
Fail: Number Total of Fail, Full, Int, 40
PassP: Percentage of Passed, Full, Int, 80

BYear: Batch Year, Long, Str, 2019-2020
ODEV: Odd or Even, Short, Str, Even



Each Row --> For i in Subjects:
Subject - Note: There is also the "KeyF" Variant of this, which means
                that it is the ****FINAL**** Subject. This is very Special.
                This means that this should be the last row.
----------------------------------------------

SubjectCodeT: Subject code i, Short, Str, 17CS51
TeachersNameT: Teachers Name For Subject i, Short, Str, Prof. Kunal Singh
AppT: Appeared Total for Subject i, Full, Int, 150
FailT: Appeared Total for Subject i, Full, Int, 40
R1: FCD for Subject i, Full, Int, 10
R2: FC for Subject i, Full, Int, 20
R3: SC for Subject i, Full, Int, 20
PPT: Pass Percentage for Subject i, Full, Int, 20
-----------------------------------------------

Please follow the above Keys for Mail Merge.
"""
from typing import IO
from tempfile import TemporaryFile

from mailmerge import MailMerge
from sqlalchemy.orm import Session

from ..Config import resources_template_path
from ..crud import get_subject_batch_sem_list
from .fillmain import __fill_main
from .fillsub import __fill_subject


def get_docx(
    db: Session, batch: int, dept: str, sem: int, ret_file: IO = TemporaryFile()
):
    # Steps:
    # 1. Get the Subjects for that year.
    # 2. Get the Main Information For that year, Mail Merge.
    subjects = get_subject_batch_sem_list(db, batch, sem)
    main_info = __fill_main(db, batch, dept, sem)
    sub_info = [__fill_subject(db, subcode, batch, dept) for subcode in subjects]
    last_sub = {}
    for (k, v) in sub_info[-1].items():
        last_sub[k + "F"] = v
    last_sub_info = [last_sub]

    with MailMerge(resources_template_path) as document:
        document.merge(**main_info)
        document.merge_rows("SubjectCodeT", sub_info[: len(sub_info) - 1])
        document.merge_rows("SubjectCodeTF", last_sub_info)

        document.write(ret_file)

    return ret_file
