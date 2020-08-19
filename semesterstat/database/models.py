from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .database import engine

# Base Model
Base = declarative_base()


class Department(Base):
    __tablename__ = "department"

    Code = Column(String, primary_key=True, index=True)
    Name = Column(String)
    Subjects = relationship("Subject")
    Students = relationship("Student")


class BatchSchemeInfo(Base):
    __tablename__ = "batchschemeinfo"

    Batch = Column(Integer, primary_key=True)
    Scheme = Column(Integer)


class Student(Base):
    __tablename__ = "student"

    Usn = Column(String, primary_key=True, index=True)
    Name = Column(String)
    Batch = Column(Integer)
    Department = Column(
        String, ForeignKey("department.Code", onupdate="CASCADE", ondelete="CASCADE")
    )

    Scores = relationship("Score")


class Subject(Base):
    __tablename__ = "subject"

    Code = Column(String(11), primary_key=True, index=True)
    Name = Column(String)
    Semester = Column(Integer)
    Scheme = Column(Integer)
    Department = Column(
        String, ForeignKey("department.Code", onupdate="CASCADE", ondelete="CASCADE")
    )


class Score(Base):
    __tablename__ = "score"

    Usn = Column(String(10), ForeignKey("student.Usn"), primary_key=True, index=True)
    SubjectCode = Column(
        String(11),
        ForeignKey("subject.Code", onupdate="CASCADE"),
        primary_key=True,
        index=True,
    )
    Internals = Column(Integer)
    Externals = Column(Integer)


# Create all of the Tables.
Base.metadata.create_all(bind=engine)
