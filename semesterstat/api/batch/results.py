from fastapi import APIRouter
from pydantic import BaseModel
from ...database import Score
from playhouse.shortcuts import model_to_dict
from ...common.query import get_scheme, get_student_usn_list, get_subject_list

results = APIRouter()


class ScoreModel(BaseModel):
    usn: str
    subject_code: str
    internals: int
    externals: int


@results.get("/{department}/{batch}/{semester}", response_model=ScoreModel)
async def get_batch_results(department: str, batch: str, semester: int):
    scheme = get_scheme(batch)

    usn_list = get_student_usn_list(batch, department)

    subject_code_list = get_subject_list(semester, scheme)

    return [
        model_to_dict(x, recurse=False)
        for x in Score.select()
        .where(
            (
                Score.ScoreSerialNumber.in_(usn_list)
                & (Score.ScoreSubjectCode.in_(subject_code_list))
            )
        )
        .objects()
    ]
