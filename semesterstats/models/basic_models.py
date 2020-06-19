from peewee import (
    Model,
    CharField,
    TextField,
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

    class Meta:
        primary_key = CompositeKey("TeacherUSN", "TeacherBatch")


class Score(BaseModel):
    ScoreSerialNumber = ForeignKeyField(Student, field=Student.StudentUSN)
    ScoreSubjectCode = ForeignKeyField(Subject, field=Subject.SubjectCode)
    ScoreSemester = IntegerField()
    ScoreInternals = IntegerField()
    ScoreExternals = IntegerField()

    class Meta:
        primary_key = CompositeKey("ScoreSerialNumber", "ScoreSubjectCode")


class Backlog(BaseModel):
    BacklogSerialNumber = ForeignKeyField(Student, field=Student.StudentUSN)
    BacklogSubjectCode = ForeignKeyField(Subject, field=Subject.SubjectCode)
    BacklogSemester = IntegerField()
    BacklogInternals = IntegerField()
    BacklogExternals = IntegerField()
