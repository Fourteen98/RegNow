import uuid
from enum import Relationship
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Guardian(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    middle_name: str
    relationship: Relationship
    student_id: int = Field(foriegn_key="students.id")
