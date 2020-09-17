from .common import get_scheme

from .batch import (
    get_batch_aggregate,
    get_batch_backlog,
    get_batch_detained_students,
    get_batch_scores,
    get_batch_students,
    get_batch_students_usn,
    is_batch_exists,
)
from .dept import (
    get_dept_by_code,
    get_dept_by_name,
    get_dept_students,
    get_dept_subjects,
    is_dept_exist,
    put_department,
    update_department,
)
from .student import (
    get_student,
    get_student_backlogs,
    get_student_scores,
    get_student_scores_by_semester,
    get_student_subject,
    is_student_exists,
    put_student,
    update_student,
)
from .subject import (
    get_subject,
    is_subject_exist,
    is_subjects_exists,
    put_subject,
    update_subject,
)

from .bulk import (
    put_department_bulk,
    put_score_bulk,
    put_student_bulk,
    put_subject_bulk,
)

__all__ = [
    "get_batch_aggregate",
    "get_batch_backlog",
    "get_batch_scores",
    "get_batch_students",
    "get_batch_students_usn",
    "get_batch_detained_students",
    "get_scheme",
    "is_batch_exists",
    "get_dept_by_code",
    "get_dept_by_name",
    "get_dept_students",
    "get_dept_subjects",
    "is_dept_exist",
    "update_department",
    "put_department",
    "get_student",
    "get_student_backlogs",
    "get_student_scores",
    "get_student_scores_by_semester",
    "get_student_subject",
    "is_student_exists",
    "put_student",
    "update_student",
    "get_subject",
    "put_subject",
    "update_subject",
    "is_subject_exist",
    "is_subjects_exists",
]
