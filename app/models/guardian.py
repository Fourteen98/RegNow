import uuid
from typing import Optional

from sqlmodel import Field, SQLModel

from app.enum.relationship import Relationship


class Guardian(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    middle_name: str
    relationship: Relationship
    student_id: int = Field(foreign_key="students.id", index=True)
