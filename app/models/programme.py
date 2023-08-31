from sqlmodel import SQLModel, Field, ForeignKey

from .student import Student

import uuid

from .enums import ProgrammeName, Stream, EntryLevel, Hall


class Programme(SQLModel, table=True):
    __tablename__ = 'programmes'
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    student_id: int = Field(ForeignKey("students.id"))
    programme_name: ProgrammeName
    stream: Stream
    entry_level: EntryLevel
    hall: Hall

    student: Student
