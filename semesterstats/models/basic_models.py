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


class Score(BaseModel):
    ScoreSerialNumber = ForeignKeyField(Student, field=Student.SerialNumber)
    ScoreSubjectCode = ForeignKeyField(Subject, field=Subject.SubjectCode)
    ScoreYear = IntegerField()
    ScoreYearIndicator = BooleanField()
    ScoreInternals = IntegerField()
    ScoreExternals = IntegerField()

    class Meta:
        primary_key = CompositeKey("SerialNumber", "SubjectCode")


class Backlog(BaseModel):
    BacklogSerialNumber = ForeignKeyField(Student, field=Student.SerialNumber)
    BacklogSubjectCode = ForeignKeyField(Subject, field=Subject.SubjectCode)
    BacklogYear = IntegerField()
    BacklogYearIndicator = BooleanField()
    BacklogInternals = IntegerField()
    BacklogExternals = IntegerField()

    class Meta:
        primary_key = CompositeKey("Year", "YearIndicator")
