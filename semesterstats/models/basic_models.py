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
    SerialNumber = FixedCharField(10, primary_key=True)
    Name = TextField()
    Batch = IntegerField()
    Department = ForeignKeyField(
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
    TeacherUsn = ForeignKeyField(TeacherDetails, field=TeacherDetails.TeacherUSN)
    Batch = IntegerField()


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


class ParsedTable(BaseModel):
    Department = ForeignKeyField(
        DepartmentDetails, field=DepartmentDetails.DepartmentCode
    )
    Batch = ForeignKeyField(BatchSchemeInfo, field=BatchSchemeInfo.Batch)
    Semester = IntegerField()
    Arrear = BooleanField()

    class Meta:
        primary_key = CompositeKey("Department", "Batch", "Semester", "Arrear")
