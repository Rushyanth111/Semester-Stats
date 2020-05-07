from peewee import (
    Model,
    CharField,
    TextField,
    DateField,
    BooleanField,
    IntegerField,
    ForeignKeyField,
    CompositeKey,
    SqliteDatabase,
)


db = SqliteDatabase("imported/data.db")


class BaseModel(Model):
    class Meta:
        database = db


class StudentDetails(BaseModel):
    SerialNumber = CharField(11, primary_key=True)
    Name = TextField()
    Scheme = CharField(2)


class SubjectDetails(BaseModel):
    SubjectCode = CharField(7, primary_key=True)
    SubjectName = TextField()
    SubjectSemester = IntegerField()


class SubjectScore(BaseModel):
    SerialNumber = ForeignKeyField(StudentDetails, field=StudentDetails.SerialNumber)
    SubjectCode = ForeignKeyField(SubjectDetails, field=SubjectDetails.SubjectCode)
    Year = IntegerField()
    YearIndicator = BooleanField()
    Internals = IntegerField()
    Externals = IntegerField()

    class Meta:
        primary_key = CompositeKey("SerialNumber", "SubjectCode")


class BacklogSubjectScore(BaseModel):
    Year = IntegerField()
    YearIndicator = BooleanField()
    SerialNumber = ForeignKeyField(StudentDetails, field=StudentDetails.SerialNumber)
    SubjectCode = ForeignKeyField(SubjectDetails, field=SubjectDetails.SubjectCode)
    Internals = IntegerField()
    Externals = IntegerField()

    class Meta:
        primary_key = CompositeKey("Year", "YearIndicator")


db.connect()
db.create_tables([StudentDetails, SubjectDetails, SubjectScore, BacklogSubjectScore])
