from fastapi import APIRouter
from fastapi.responses import FileResponse
from ...config import db
from ...docgen import docs_mail_merge_gen


batch = APIRouter()


@batch.get("/{department}/{batch}/{semester}/detail")
def get_batch_detail(department: str, semester: int, batch: int):
    return db.external_get_batch_semester_scores(batch, department, semester)


@batch.get("/{department}/{batch}/{semester}/summary")
def get_batch_summary(department: str, semester: int, batch: int):
    return db.external_get_batch_semester_summary(batch, department, semester)


@batch.get("/{department}/{batch}/list")
def get_batch_students(department: str, batch: int):
    return db.external_get_batch_details(batch, department)


@batch.get("/{department}/{batch}/backlogs")
def get_batch_backlog(department: str, batch: int):
    return db.external_get_batch_backlogs(batch, department)


@batch.get("/{department}/{batch}/{semester}/sfile")
def get_batch_summary_file(department: str, semester: int, batch: int):
    docs_mail_merge_gen(batch, semester, department)
    return FileResponse(path="demo.docx", media_type="docx", filename="Report.docx")
