from peewee import (
    Model,
    CharField,
    TextField,
    IntegerField,
    ForeignKeyField,
    CompositeKey,
    AutoField,
    FixedCharField,
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
    Code = FixedCharField(3, primary_key=True)
    Name = TextField()


class BatchSchemeInfo(BaseModel):
    Batch = IntegerField(primary_key=True)
    Scheme = IntegerField()


class Student(BaseModel):
    Usn = FixedCharField(10, primary_key=True)
    Name = TextField()
    Batch = IntegerField()
    Department = ForeignKeyField(Department, field=Department.Code)


class Subject(BaseModel):
    Code = CharField(7, primary_key=True)
    Name = TextField()
    Semester = IntegerField()
    Scheme = IntegerField()
    Department = ForeignKeyField(Department, field=Department.Code)


class Teacher(BaseModel):
    Usn = AutoField()
    Name = TextField()


class TeacherTaught(BaseModel):
    Usn = ForeignKeyField(Teacher, field=Teacher.Usn)
    Batch = IntegerField()
    Subject = ForeignKeyField(Subject, field=Subject.Code)


class Score(BaseModel):
    Usn = ForeignKeyField(Student, field=Student.Usn, on_update="CASCADE")
    SubjectCode = ForeignKeyField(Subject, field=Subject.Code, on_update="CASCADE")
    Internals = IntegerField()
    Externals = IntegerField()

    class Meta:
        primary_key = CompositeKey("Usn", "SubjectCode")
        indexes = ((("Usn", "SubjectCode"), True),)


class BacklogHistory(BaseModel):
    Usn = ForeignKeyField(Student, field=Student.Usn)
    SubjectCode = ForeignKeyField(Subject, field=Subject.Code)
    Internals = IntegerField()
    Externals = IntegerField()

    class Meta:
        indexes = ((("Usn", "SubjectCode"), False),)
        primary_key = False


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
        fields=[Department.Code, Department.Name],
    ).execute()


logger.info("Creating Trigger for Table: Score")

trigger_string = """
create trigger if not exists score_1  after update
    on {}
    when {}
BEGIN
    Insert into {}({}) values ({});
END;
"""
formatted_trigger = trigger_string.format(
    Score._meta.table_name,
    "(old.Internals+old.Externals) < (new.Internals+new.Externals)",
    BacklogHistory._meta.table_name,
    ",".join(
        [str(feild.name) for feild in db.get_columns(BacklogHistory._meta.table_name)]
    ),
    ",".join(
        ["old." + str(feild.name) for feild in db.get_columns(Score._meta.table_name)]
    ),
)

logger.debug("Processing Trigger: {}", formatted_trigger)

db.execute_sql(formatted_trigger)

logger.info("Database Initalized with: Tables, Triggers, and Department Information")
