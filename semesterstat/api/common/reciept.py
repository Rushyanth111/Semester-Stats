from pydantic import BaseModel


class DeparmentReceipt(BaseModel):
    Name: str
    Code: str
