from fastapi import status
from fastapi.exceptions import HTTPException


class DoesNotExistException(HTTPException):
    def __init__(self, detail: str = None):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class BatchDoesNotExist(DoesNotExistException):
    def __init__(self) -> None:
        super().__init__(detail="Batch Does Not Exist")


class DeptDoesNotExist(DoesNotExistException):
    def __init__(self) -> None:
        super().__init__(detail="Dept Does Not Exist")


class StudentDoesNotExist(DoesNotExistException):
    def __init__(self) -> None:
        super().__init__(detail="Student Does Not Exist")


class SubjectDoesNotExist(DoesNotExistException):
    def __init__(self) -> None:
        super().__init__(detail="Subject Does Not Exist")


class ConflictException(HTTPException):
    def __init__(self, detail: str = None) -> None:
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)


class BatchConflictException(ConflictException):
    def __init__(self, batch: int) -> None:
        super().__init__(detail="{} Already Exists".format(batch))


class DeptConflictException(ConflictException):
    def __init__(self, dept: int) -> None:
        super().__init__(detail="{} Already Exists".format(dept))


class StudentConflictException(ConflictException):
    def __init__(self, usn: int) -> None:
        super().__init__(detail="{} Already Exists".format(usn))


class SubjectConflictException(ConflictException):
    def __init__(self, subcode: int) -> None:
        super().__init__(detail="{} Already Exists".format(subcode))


class NoResultFoundForQuery(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, detail="No Records Exist"
        )
