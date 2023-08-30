from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates
from sqlalchemy_utils import ChoiceType
from datetime import date
from alembic import command
from alembic.config import Config

from sqlmodel import Column, Field, SQLModel


class Program(SQLModel, table=True):
    __tablename__ = 'programs'
    id = Field(Integer, primary_key=True)
    student_id = Field(Integer, ForeignKey('students.id'), nullable=False)
    programme_name = Field(Enum('Computer Science', 'Computer Networking', 'Marketing', 'Financal Accounting', name='programme_name_enum'), nullable=False)
    stream = Field(Enum('Stream X', 'Stream Y', 'Stream Z', name='stream_enum'), nullable=False)
    entry_level = Field(Enum('Level 1', 'Level 2', 'Level 3', name='entry_level_enum'), nullable=False)
    hall = Field(Enum('Hall A', 'Hall B', 'Hall C', name='hall_enum'), nullable=False)
    student = relationship("Student", back_populates="programs")

class Student(SQLModel, table=True):
    __tablename__ = 'students'
    id = Field(Integer, primary_key=True)
    name = Field(String, nullable=False)
    programs = relationship("Program", back_populates="student")

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty.")
        return name

