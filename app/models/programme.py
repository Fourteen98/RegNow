import uuid
from sqlmodel import Column, Field, ForeignKey, Enum, relationship, SQLModel


class Student(SQLModel, table=True):
    __tablename__ = 'students'
    
    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    
    programs: list["Program"] = relationship("Program", back_populates="student")


class Program(SQLModel, table=True):
    __tablename__ = 'programs'
    
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    student_id: int = Field(ForeignKey('students.id'), nullable=False)
    programme_name: str = Field(Enum('Program A', 'Program B', name='programme_name_enum'), nullable=False)
    stream: str = Field(Enum('Stream X', 'Stream Y', 'Stream Z', name='stream_enum'), nullable=False)
    entry_level: str = Field(Enum('Level 1', 'Level 2', 'Level 3', name='entry_level_enum'), nullable=False)
    hall: str = Field(Enum('Hall A', 'Hall B', 'Hall C', name='hall_enum'), nullable=False)
    
    student: Student = relationship("Student", back_populates="programs")
