from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..common import Report
from ..database import get_db

bulk = APIRouter()

"""
The Bulk API Router handles the Bulk Transactions of the User, namely Updating Reports
and Adding new Reports.

"""


@bulk.post("/", status_code=status.HTTP_201_CREATED, deprecated=True)
async def upsert_bulk(reports: List[Report], db: Session = Depends(get_db)):
    pass
