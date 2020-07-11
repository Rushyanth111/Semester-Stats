from peewee import SqliteDatabase, fn
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

    def external_get_student_backlogs_history(
        self, usn: str
    ) -> List[BacklogScoreModel]:
        return [
            BacklogScoreModel.construct(**model_to_dict(x, recurse=False))
            for x in Backlog.select().where((Backlog.BacklogSerialNumber == usn))
        ]

    def external_get_student_backlogs(self, usn: str) -> List[ScoreModel]:
        return [
            ScoreModel.construct(**model_to_dict(x, recurse=False))
            for x in Score.select().where(
                (Score.ScoreInternals + Score.ScoreExternals < 45)
                & (Score.ScoreSerialNumber == usn)
            )
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

    def external_get_batch_backlogs(self, batch: int, department: str):
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

        usn_list = Student.select(Student.StudentUSN).where(
            (Student.StudentDepartment == department) & (Student.StudentBatch == batch)
        )

        return convert_to_simple(
            [
                ScoreModel.construct(**model_to_dict(x, recurse=False))
                for x in Score.select()
                .where(
                    (
                        Score.ScoreSerialNumber.in_(usn_list)
                        & (Score.ScoreInternals + Score.ScoreExternals < 45)
                    )
                )
                .objects()
            ]
        )

    def external_get_batch_detained(self, batch: int, department: str):
        usn_list = Student.select(Student.StudentUSN).where(
            (Student.StudentDepartment == department) & (Student.StudentBatch == batch)
        )

        return [
            ScoreModel.construct(**model_to_dict(x, recurse=False)).ScoreSerialNumber
            for x in Score.select()
            .where(
                (
                    Score.ScoreSerialNumber.in_(usn_list)
                    & (Score.ScoreInternals + Score.ScoreExternals < 45)
                )
            )
            .group_by(Score.ScoreSerialNumber)
            .having(fn.count(Score.ScoreSerialNumber) > 4)
            .objects()
        ]

    def external_get_batch_semester_summary(
        self, batch: int, department: str, semester: int
    ):
        def get_class():
            pass

        final_information = {}

        scheme = BatchSchemeInfo.select(BatchSchemeInfo.Scheme).where(
            (BatchSchemeInfo.Batch == batch)
        )

        usn_list = Student.select(Student.StudentUSN).where(
            (Student.StudentDepartment == department) & (Student.StudentBatch == batch)
        )

        subject_code_list = Subject.select(Subject.SubjectCode).where(
            (Subject.SubjectScheme == scheme)
            & (Subject.SubjectSemester == semester)
            & (Subject.SubjectDepartment == department)
        )

        fcd_count = (
            Score.select()
            .where(
                (
                    (Score.ScoreSerialNumber.in_(usn_list))
                    & (Score.ScoreSubjectCode.in_(subject_code_list))
                    & ((Score.ScoreExternals + Score.ScoreInternals) > 70)
                )
            )
            .group_by(Score.ScoreSerialNumber)
            .having((fn.SUM(Score.ScoreInternals) + fn.SUM(Score.ScoreExternals)) > 600)
        )

        fc_count = (
            Score.select()
            .where(
                (
                    (Score.ScoreSerialNumber.in_(usn_list))
                    & (Score.ScoreSubjectCode.in_(subject_code_list))
                )
            )
            .group_by(Score.ScoreSerialNumber)
            .having(
                (fn.SUM(Score.ScoreInternals) + fn.SUM(Score.ScoreExternals)).between(
                    450, 600
                )
            )
        )

        sc_count = (
            Score.select()
            .where(
                (
                    (Score.ScoreSerialNumber.in_(usn_list))
                    & (Score.ScoreSubjectCode.in_(subject_code_list))
                )
            )
            .group_by(Score.ScoreSerialNumber)
            .having(
                (fn.SUM(Score.ScoreInternals) + fn.SUM(Score.ScoreExternals)).between(
                    300, 450
                )
            )
        )

        fail_count = (
            Score.select()
            .where(
                (
                    (Score.ScoreSerialNumber.in_(usn_list))
                    & (Score.ScoreSubjectCode.in_(subject_code_list))
                )
            )
            .group_by(Score.ScoreSerialNumber)
            .having((fn.SUM(Score.ScoreInternals) + fn.SUM(Score.ScoreExternals)) < 350)
        )

        sub_fail_count_array = []
        sub_pass_count_array = []
        sub_fcd_count_array = []
        sub_fc_count_array = []
        sub_sc_count_array = []

        for subject_code in subject_code_list:
            subject_code = subject_code.SubjectCode
            sub_fcd_count = Score.select().where(
                (
                    (Score.ScoreSerialNumber.in_(usn_list))
                    & (Score.ScoreSubjectCode == subject_code)
                    & (Score.ScoreExternals + Score.ScoreInternals > 70)
                )
            )

            sub_fc_count = Score.select().where(
                (
                    (Score.ScoreSerialNumber.in_(usn_list))
                    & (Score.ScoreSubjectCode == subject_code)
                    & ((Score.ScoreExternals + Score.ScoreInternals).between(60, 70))
                )
            )

            sub_sc_count = Score.select().where(
                (
                    (Score.ScoreSerialNumber.in_(usn_list))
                    & (Score.ScoreSubjectCode == subject_code)
                    & ((Score.ScoreExternals + Score.ScoreInternals).between(45, 60))
                )
            )

            sub_fail_count = Score.select().where(
                (
                    (Score.ScoreSerialNumber.in_(usn_list))
                    & (Score.ScoreSubjectCode == subject_code)
                    & ((Score.ScoreExternals + Score.ScoreInternals) < 45)
                )
            )
            final_information[subject_code] = {}
            final_information[subject_code]["TotalAttendees"] = usn_list.count()
            final_information[subject_code]["FCD"] = sub_fcd_count.count()
            final_information[subject_code]["FC"] = sub_fc_count.count()
            final_information[subject_code]["SC"] = sub_sc_count.count()
            final_information[subject_code]["PassPercentage"] = (
                (usn_list.count() - sub_fail_count.count()) * 100 / usn_list.count()
            )
            final_information[subject_code]["FailPercentage"] = 100 - (
                (usn_list.count() - sub_fail_count.count()) * 100 / usn_list.count()
            )
            final_information[subject_code]["Pass"] = (
                usn_list.count() - sub_fail_count.count()
            )
            final_information[subject_code]["Fail"] = sub_fail_count.count()
            sub_fail_count_array.append(sub_fail_count.count())
            sub_fcd_count_array.append(sub_fcd_count.count())
            sub_fc_count_array.append(sub_fc_count.count())
            sub_sc_count_array.append(sub_sc_count.count())
            sub_pass_count_array.append(usn_list.count() - sub_fail_count.count())

        final_information["SubjectCodes"] = [x.SubjectCode for x in subject_code_list]
        final_information["SubjectFailArray"] = sub_fail_count_array
        final_information["SubjectPassArray"] = sub_pass_count_array
        final_information["SubjectFCDArray"] = sub_fcd_count_array
        final_information["SubjectFCArray"] = sub_fc_count_array
        final_information["SubjectSCArray"] = sub_sc_count_array
        final_information["TotalAttendees"] = usn_list.count()
        final_information["FCD"] = fcd_count.count()
        final_information["FC"] = fc_count.count()
        final_information["SC"] = sc_count.count()
        final_information["Pass"] = usn_list.count() - fail_count.count()
        final_information["Fail"] = fail_count.count()
        final_information["PassPercentage"] = (
            (usn_list.count() - fail_count.count()) * 100 / usn_list.count()
        )
        final_information["FailPercentage"] = 100 - (
            (usn_list.count() - fail_count.count()) * 100 / usn_list.count()
        )

        return final_information
