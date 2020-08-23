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

__all__ = [
    "BatchQuery",
    "get_dept_by_code",
    "get_dept_by_name",
    "get_dept_students",
    "get_dept_subjects",
    "is_dept_exist",
]
