# This file contains the entire interface bundled together as in seamlessly integrated
import json

from peewee import SqliteDatabase

from ..logging import AppLog
from .basic_models import (
    proxy,
    Backlog,
    BatchSchemeInfo,
    Department,
    Student,
    Subject,
    Score,
    Teacher,
    TeacherTaught,
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
                Department,
                BatchSchemeInfo,
                Subject,
                Student,
                Score,
                Backlog,
                Teacher,
                TeacherTaught,
            ]
        )

        self.__init_department_details()

    def __init_department_details(self):
        if Department.select().count() == 0:
            AppLog.info("Inserting Department Details!")
            with self.db.atomic():
                with open("FormattedData/Departments.json") as f:
                    DepartmentCodeDictionary = json.loads(f.read())
                    Department.insert_many(
                        set(
                            zip(
                                DepartmentCodeDictionary.keys(),
                                DepartmentCodeDictionary.values(),
                            )
                        ),
                        fields=[Department.DepartmentCode, Department.DepartmentName],
                    ).execute()
        else:
            AppLog.info("Skipping the Insertion of Department Details")
