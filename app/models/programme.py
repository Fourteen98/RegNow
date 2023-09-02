from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from app.enum.entry_level import EntryLevel
from app.enum.hall import Hall
from app.enum.programme import Programme as ProgrammeEnum
from app.enum.stream import Stream


class Programme(SQLModel, table=True):
    __tablename__ = "programmes"

    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    programme_name: ProgrammeEnum
    stream: Stream
    entry_level: EntryLevel
    hall: Hall
    student_id: str = Field(
        foreign_key="students.index_number", unique=True, index=True)
    created_at: Optional[datetime] = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=datetime.now())


class ProgrammeCreate(SQLModel):
    programme_name: ProgrammeEnum
    stream: Stream
    entry_level: EntryLevel
    hall: Hall
    student_id: int = Field(foreign_key="students.id", unique=True, index=True)
