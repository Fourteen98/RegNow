import uuid

from sqlmodel import Column, Field, SQLModel


class Program(SQLModel, table=True):
    __tablename__ = 'programs'
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    n student_id = Field(Integer, ForeignKey('students.id'), nullable=False)
    programme_name = Field(Enum('Program A', 'Program B', name='programme_name_enum'), nullable=False)
    stream = Field(Enum('Stream X', 'Stream Y', 'Stream Z', name='stream_enum'), nullable=False)
    entry_level = Field(Enum('Level 1', 'Level 2', 'Level 3', name='entry_level_enum'), nullable=False)
    hall = Field(Enum('Hall A', 'Hall B', 'Hall C', name='hall_enum'), nullable=False)
    
    student = relationship("Student", back_populates="programs")
