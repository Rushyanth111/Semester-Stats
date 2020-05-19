# This file contains the entire interface bundled together as in seamlessly integrated
import json

from peewee import SqliteDatabase

from ..logging import AppLog
from .basic_models import (
    proxy,
    BacklogSubjectScore,
    BatchSchemeInfo,
    DepartmentDetails,
    ParsedTable,
    StudentDetails,
    SubjectDetails,
    SubjectScore,
    TeacherDetails,
    TeacherTaughtDetails,
)
from .get_interface import GetInterface
from .insert_interface import InsertInterface

DepartmentCodeDictionary = {}


class ModelInterface(GetInterface, InsertInterface):
    def __init__(
        self, database_name=":memory:", pragmas={}, datafile_path="FormattedData"
    ):
        super().__init__()
        self.database_name = database_name
        self.pragmas = pragmas

        self.db = SqliteDatabase(
            self.database_name,
            pragmas={
                "journal_mode": "wal",
                "cache_size": "-1",
                "foreign_keys": "1",
                "ignore_check_constraints": "0",
                "recursive_triggers": "ON",
            },
        )
        proxy.initialize(self.db)
        self.db.connect()

        self.db.create_tables(
            [
                BacklogSubjectScore,
                BatchSchemeInfo,
                DepartmentDetails,
                ParsedTable,
                StudentDetails,
                SubjectDetails,
                SubjectScore,
                TeacherDetails,
                TeacherTaughtDetails,
            ]
        )

        self.__init_department_details()

    def __init_department_details(self):
        if len(list(DepartmentDetails.select())) == 0:
            AppLog.info("Inserting Department Details!")
            with self.db.atomic():
                with open("FormattedData/Departments.json") as f:
                    DepartmentCodeDictionary = json.loads(f.read())
                    DepartmentDetails.insert_many(
                        set(
                            zip(
                                DepartmentCodeDictionary.keys(),
                                DepartmentCodeDictionary.values(),
                            )
                        ),
                        fields=[
                            DepartmentDetails.DepartmentCode,
                            DepartmentDetails.DepartmentName,
                        ],
                    ).execute()
        else:
            AppLog.info("Skipping the Insertion of Department Details")
