from .batch import BatchQuery

from .dept import (
    get_dept_by_code,
    get_dept_by_name,
    get_dept_students,
    get_dept_subjects,
    is_dept_exist,
    update_department,
    put_department,
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

__all__ = [
    "BatchQuery",
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
]
