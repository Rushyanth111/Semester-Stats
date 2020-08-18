from pydantic import BaseModel


class DepartmentReceipt(BaseModel):
    Name: str
    Code: str
