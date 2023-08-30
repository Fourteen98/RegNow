from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates
from sqlalchemy_utils import ChoiceType
from datetime import date
from alembic import command
from alembic.config import Config

# Create an SQLite in-memory database
engine = create_engine('sqlite:///programme_database.db', echo=True)

Base = declarative_base()

class Program(Base):
    __tablename__ = 'programs'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    programme_name = Column(Enum('Program A', 'Program B', name='programme_name_enum'), nullable=False)
    stream = Column(Enum('Stream X', 'Stream Y', 'Stream Z', name='stream_enum'), nullable=False)
    entry_level = Column(Enum('Level 1', 'Level 2', 'Level 3', name='entry_level_enum'), nullable=False)
    hall = Column(Enum('Hall A', 'Hall B', 'Hall C', name='hall_enum'), nullable=False)
    
    student = relationship("Student", back_populates="programs")

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    programs = relationship("Program", back_populates="student")

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty.")
        return name

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example usage: Adding a student and program
new_student = Student(name="John Doe")
session.add(new_student)
session.commit()

new_program = Program(student=new_student, programme_name='Program A', stream='Stream X', entry_level='Level 1', hall='Hall A')
session.add(new_program)
session.commit()

# Generate Alembic migration
alembic_cfg = Config("alembic.ini")  # Point this to your Alembic configuration file
alembic_cfg.set_main_option("script_location", "your_script_location")
command.revision(alembic_cfg, autogenerate=True, message="Create students and programs tables")

session.close()
