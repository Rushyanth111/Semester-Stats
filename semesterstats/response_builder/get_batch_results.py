from ..config import db


def get_batch_results(batch: int, semester: int, department: str):
    return db.get_scores(batch, semester, department)
