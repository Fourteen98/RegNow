import uuid

from sqlmodel import Column, Field, SQLModel


class Programme(SQLModel, table=True):
   __tablename__ = 'programs'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    programme_name = Column(Enum('Computer Science', 'Computer Networking', name='programme_name_enum'), nullable=False)
    stream = Column(Enum('Stream X', 'Stream Y', 'Stream Z', name='stream_enum'), nullable=False)
    entry_level = Column(Enum('Level 1', 'Level 2', 'Level 3', name='entry_level_enum'), nullable=False)
    hall = Column(Enum('Hall A', 'Hall B', 'Hall C', name='hall_enum'), nullable=False)
    
    student = relationship("Student", back_populates="programs")
