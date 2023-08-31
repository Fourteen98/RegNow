from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from app.enum.entry_level import EntryLevel
from app.enum.hall import Hall
from app.enum.programme import Programme
from app.enum.stream import Stream


class BirdCreate(SQLModel):
    name: str = Field(index=True, max_length=50, nullable=False)
    color: str


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
    student_id: int = Field(foreign_key="students.id", unique=True, index=True)
