from semesterstat.docgen import get_docx
import os


def test_genned(db):
    get_docx(db, 2015, "CS", 1, "test.docx")
    assert os.path.exists("test.docx")

    os.remove("test.docx")
