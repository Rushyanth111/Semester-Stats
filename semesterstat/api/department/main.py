from fastapi import APIRouter
from .get_dept import get_dept

dept = APIRouter()

dept.include_router(get_dept)
