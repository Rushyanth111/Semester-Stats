from peewee import (
    Model,
    CharField,
    TextField,
    IntegerField,
    ForeignKeyField,
    CompositeKey,
    AutoField,
    FixedCharField,
    BooleanField,
    SqliteDatabase,
)
from ..Config import database_store_path, formatted_data_path
from loguru import logger
import json


# Define the database:
db = SqliteDatabase(
    database_store_path,
    pragmas={
        "journal_mode": "wal",
        "cache_size": "-1",
        "foreign_keys": "1",
        "ignore_check_constraints": "0",
        "recursive_triggers": "ON",
    },
)


# Create a BaseModel.
class BaseModel(Model):
    class Meta:
        database = db


class Department(BaseModel):
    DepartmentCode = FixedCharField(3, primary_key=True)
    DepartmentName = TextField()


class BatchSchemeInfo(BaseModel):
    Batch = IntegerField(primary_key=True)
    Scheme = IntegerField()


class Student(BaseModel):
    StudentUSN = FixedCharField(10, primary_key=True)
    StudentName = TextField()
    StudentBatch = IntegerField()
    StudentDepartment = ForeignKeyField(Department, field=Department.DepartmentCode)


class Subject(BaseModel):
    SubjectCode = CharField(7, primary_key=True)
    SubjectName = TextField()
    SubjectSemester = IntegerField()
    SubjectScheme = IntegerField()
    SubjectDepartment = ForeignKeyField(Department, field=Department.DepartmentCode)


class Teacher(BaseModel):
    TeacherUSN = AutoField()
    TeacherName = TextField()


class TeacherTaught(BaseModel):
    TeacherUSN = ForeignKeyField(Teacher, field=Teacher.TeacherUSN)
    TeacherBatch = IntegerField()

    class Meta:
        primary_key = CompositeKey("TeacherUSN", "TeacherBatch")


class Score(BaseModel):
    ScoreSerialNumber = ForeignKeyField(Student, field=Student.StudentUSN)
    ScoreSubjectCode = ForeignKeyField(Subject, field=Subject.SubjectCode)
    ScoreInternals = IntegerField()
    ScoreExternals = IntegerField()

    class Meta:
        primary_key = CompositeKey("ScoreSerialNumber", "ScoreSubjectCode")
        indexes = ((("ScoreSerialNumber", "ScoreSubjectCode"), True),)


class BacklogHistory(BaseModel):
    BacklogSerialNumber = ForeignKeyField(Student, field=Student.StudentUSN)
    BacklogSubjectCode = ForeignKeyField(Subject, field=Subject.SubjectCode)
    BacklogInternals = IntegerField()
    BacklogExternals = IntegerField()

    class Meta:
        indexes = ((("BacklogSerialNumber", "BacklogSubjectCode"), False),)
        primary_key = False


class Parsed(BaseModel):
    ParsedDepartment = FixedCharField(3)
    ParsedScheme = IntegerField()
    ParsedBatch = IntegerField()
    ParsedSemester = IntegerField()
    ParsedArrear = BooleanField()

    class Meta:
        primary_key = CompositeKey(
            "ParsedScheme",
            "ParsedBatch",
            "ParsedSemester",
            "ParsedDepartment",
            "ParsedArrear",
        )


logger.info("Creating Tables if not existing.")
db.connect()
db.create_tables(
    [
        Department,
        BatchSchemeInfo,
        Teacher,
        TeacherTaught,
        Student,
        Subject,
        Score,
        BacklogHistory,
    ]
)

logger.info("Inserting Department Details")

with open(formatted_data_path + "/Departments.json") as file, db.atomic():
    dep_codes = json.loads(file.read())
    Department.insert_many(
        set(zip(dep_codes.keys(), dep_codes.values(),)),
        fields=[Department.DepartmentCode, Department.DepartmentName],
    ).execute()


logger.info("Creating Trigger for Table: Score")

trigger_string = """
create trigger score_1 if not exists after update
    on {}
    when {}
BEGIN
    Insert into {}({}) values ({});
END;
"""
db.execute_sql(
    trigger_string.format(
        Score._meta.table_name,
        "(old.ScoreInternals + old.ScoreExternals) < (new.ScoreInternals + new.ScoreExternals)",
        BacklogHistory._meta.table_name,
        ",".join(
            [
                str(feild.name)
                for feild in db.get_columns(BacklogHistory._meta.table_name)
            ]
        ),
        ",".join(
            [
                "old." + str(feild.name)
                for feild in db.get_columns(Score._meta.table_name)
            ]
        ),
    )
)

logger.info("Database Initalized with: Tables, Triggers, and Department Information")
