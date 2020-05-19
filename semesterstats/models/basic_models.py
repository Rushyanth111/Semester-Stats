from peewee import (
    Model,
    CharField,
    TextField,
    BooleanField,
    IntegerField,
    ForeignKeyField,
    CompositeKey,
    AutoField,
    FixedCharField,
    Proxy,
)

proxy = Proxy()


class BaseModel(Model):
    class Meta:
        database = proxy


class DepartmentDetails(BaseModel):
    DepartmentCode = FixedCharField(3, primary_key=True)
    DepartmentName = TextField()


class BatchSchemeInfo(BaseModel):
    Batch = IntegerField(primary_key=True)
    Scheme = IntegerField()


class StudentDetails(BaseModel):
    StudentUSN = FixedCharField(10, primary_key=True)
    StudentName = TextField()
    StudentBatch = IntegerField()
    StudentDepartment = ForeignKeyField(
        DepartmentDetails, field=DepartmentDetails.DepartmentCode
    )


class SubjectDetails(BaseModel):
    SubjectCode = CharField(7, primary_key=True)
    SubjectName = TextField()
    SubjectSemester = IntegerField()
    SubjectScheme = IntegerField()
    SubjectDepartment = ForeignKeyField(
        DepartmentDetails, field=DepartmentDetails.DepartmentCode
    )


class TeacherDetails(BaseModel):
    TeacherUSN = AutoField()
    TeacherName = TextField()


class TeacherTaughtDetails(BaseModel):
    TeacherUSN = ForeignKeyField(TeacherDetails, field=TeacherDetails.TeacherUSN)
    TeacherBatch = IntegerField()


class SubjectScore(BaseModel):
    ScoreSerialNumber = ForeignKeyField(
        StudentDetails, field=StudentDetails.SerialNumber
    )
    ScoreSubjectCode = ForeignKeyField(SubjectDetails, field=SubjectDetails.SubjectCode)
    ScoreYear = IntegerField()
    ScoreYearIndicator = BooleanField()
    ScoreInternals = IntegerField()
    ScoreExternals = IntegerField()

    class Meta:
        primary_key = CompositeKey("SerialNumber", "SubjectCode")


class BacklogSubjectScore(BaseModel):
    ScoreSerialNumber = ForeignKeyField(
        StudentDetails, field=StudentDetails.SerialNumber
    )
    ScoreSubjectCode = ForeignKeyField(SubjectDetails, field=SubjectDetails.SubjectCode)
    ScoreYear = IntegerField()
    ScoreYearIndicator = BooleanField()
    ScoreInternals = IntegerField()
    ScoreExternals = IntegerField()

    class Meta:
        primary_key = CompositeKey("Year", "YearIndicator")
