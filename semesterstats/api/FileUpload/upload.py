from fastapi import APIRouter, UploadFile, File
from ...parser import csv_parser
import shutil

upload_route = APIRouter()


@upload_route.post("/upload")
def create_file(file: UploadFile = File(...)):
    with open("FormattedData/" + file.filename, mode="wb") as dest:
        shutil.copyfileobj(file.file, dest)

    csv_parser("FormattedData/" + file.filename)

    return {"status": "success"}
