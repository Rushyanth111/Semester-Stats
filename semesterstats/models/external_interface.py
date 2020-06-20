from peewee import SqliteDatabase
from .basic_models import (
    Department,
    BatchSchemeInfo,
    Backlog,
    Student,
    Subject,
    Score,
)
from playhouse.shortcuts import model_to_dict

from .interface_models import (
    DepartmentModel,
    ScoreModel,
    BacklogScoreModel,
    SubjectModel,
    StudentModel,
    SchemeModel,
)

from typing import List


class ExternalInterface:
    db: SqliteDatabase

    def __init__(self):
        pass

    def external_get_department(self, department: str):
        return DepartmentModel.construct(
            **model_to_dict(
                Department.select()
                .where((Department.DepartmentCode == department))
                .objects()[0],
                recurse=False,
            )
        )

    def external_get_scheme(self, batch: int) -> SchemeModel:
        return SchemeModel.construct(
            **model_to_dict(
                BatchSchemeInfo.select()
                .where((BatchSchemeInfo.Batch == batch))
                .objects()[0]
            )
        )

    def external_get_subject(self, subject_code: str):
        subject = list(
            Subject.select().where((Subject.SubjectCode == subject_code)).objects()
        )

        if len(subject) == 0:
            return None

        return SubjectModel.construct(**model_to_dict(subject[0]))

    def external_get_student_backlogs(self, usn: str) -> List[BacklogScoreModel]:
        return [
            BacklogScoreModel.construct(**model_to_dict(x, recurse=False))
            for x in Backlog.select().where((Backlog.BacklogSerialNumber == usn))
        ]

    def external_get_student(self, usn: str):
        return StudentModel.construct(
            **model_to_dict(
                Student.select().where((Student.StudentUSN == usn)).objects()[0]
            )
        )

    def external_get_student_semester_scores(self, usn: str, semester: int):
        return [
            ScoreModel.construct(**model_to_dict(x, recurse=False))
            for x in Score.select().where(
                (Score.ScoreSerialNumber == usn) & (Score.ScoreSemester == semester)
            )
        ]

    def external_get_batch_details(self, batch: int, department: str):
        return [
            StudentModel.construct(**model_to_dict(x, recurse=False))
            for x in Student.select()
            .where(
                (Student.StudentBatch == batch)
                & (Student.StudentDepartment == department)
            )
            .objects()
        ]

    def external_get_batch_semester_scores(
        self, batch: int, department: str, semester: int
    ):
        def convert_to_simple(dict_list):
            u_list = {}
            for score_record in dict_list:
                if score_record.ScoreSerialNumber not in u_list:
                    u_list[score_record.ScoreSerialNumber] = {}

                u_list[score_record.ScoreSerialNumber][
                    "USN"
                ] = score_record.ScoreSerialNumber
                u_list[score_record.ScoreSerialNumber][
                    score_record.ScoreSubjectCode
                ] = [score_record.ScoreInternals, score_record.ScoreExternals]
            return list(u_list.values())

        scheme = BatchSchemeInfo.select(BatchSchemeInfo.Scheme).where(
            (BatchSchemeInfo.Batch == batch)
        )

        usn_list = Student.select(Student.StudentUSN).where(
            (Student.StudentDepartment == department) & (Student.StudentBatch == batch)
        )

        subject_code_list = Subject.select(Subject.SubjectCode).where(
            (Subject.SubjectScheme == scheme) & (Subject.SubjectSemester == semester)
        )

        return convert_to_simple(
            [
                ScoreModel.construct(**model_to_dict(x, recurse=False))
                for x in Score.select()
                .where(
                    (
                        Score.ScoreSerialNumber.in_(usn_list)
                        & (Score.ScoreSubjectCode.in_(subject_code_list))
                    )
                )
                .objects()
            ]
        )
