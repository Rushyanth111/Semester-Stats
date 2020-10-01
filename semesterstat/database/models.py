from sqlalchemy import Column, ForeignKey, Index, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import UniqueConstraint

from .database import engine

# Base Model
Base = declarative_base()


class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Code = Column(String, unique=True, index=True)
    Name = Column(String)

    Subjects = relationship("Subject")
    Students = relationship("Student")


class BatchSchemeInfo(Base):
    __tablename__ = "batchschemeinfo"

    Batch = Column(Integer, primary_key=True)
    Scheme = Column(Integer)


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Usn = Column(String, unique=True, index=True)
    Name = Column(String)
    Batch = Column(Integer)
    Department = Column(
        String, ForeignKey("department.Code", onupdate="CASCADE", ondelete="CASCADE")
    )

    Scores = relationship("Score")

    __table_args__ = (Index("Student_IDX", "Batch", "Department", "Usn"),)


class Subject(Base):
    __tablename__ = "subject"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Code = Column(String(11), unique=True, index=True)
    Name = Column(String)
    Semester = Column(Integer)
    Scheme = Column(Integer)
    Department = Column(
        String, ForeignKey("department.Code", onupdate="CASCADE", ondelete="CASCADE")
    )
    MinExt = Column(Integer)
    MinTotal = Column(Integer)
    MaxTotal = Column(Integer)
    Credits = Column(Integer)

    __table_args__ = (Index("Subject_IDX", "Scheme", "Department", "Code"),)


class Score(Base):
    __tablename__ = "score"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Usn = Column(String(10), ForeignKey("student.Usn"), index=True)
    SubjectCode = Column(
        String(11), ForeignKey("subject.Code", onupdate="CASCADE"), index=True
    )
    Internals = Column(Integer)
    Externals = Column(Integer)

    __table_args__ = (
        Index("Score_IDX", "Usn", "SubjectCode"),
        UniqueConstraint("Usn", "SubjectCode"),
    )


# Create all of the Tables.
Base.metadata.create_all(bind=engine)
