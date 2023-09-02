from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from app.enum.entry_level import EntryLevel
from app.enum.hall import Hall
from app.enum.programme import Programme
from app.enum.relationship import Relationship
from app.enum.stream import Stream


class StudentCreate(SQLModel):
    first_name: str
    last_name: str
    middle_name: str
    gender: str
    nationality: str
    age: int
    place_of_birth: str
    current_residence: str
    email: EmailStr


class ProgrammeCreate(SQLModel):
    programme_name: Programme
    stream: Stream
    entry_level: EntryLevel
    hall: Hall
    student_id: str = Field(foreign_key="students.id", unique=True, index=True)


class GuardianCreate(SQLModel):
    first_name: str
    last_name: str
    middle_name: str
    relationship: str
    student_id: str = Field(foreign_key="students.id", index=True)


class RegisterStudentCreate(SQLModel):
    first_name: str
    last_name: str
    middle_name: str
    gender: str
    nationality: str
    age: int
    place_of_birth: str
    current_residence: str
    email: EmailStr
    programme_name: Programme
    stream: Stream
    entry_level: EntryLevel
    hall: Hall
    guardian_first_name: str
    guardian_last_name: str
    guardian_middle_name: str
    guardian_relationship: Relationship
