import uuid
from enum import Relationship
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Guardian(SQLModel, table=True):
    id int: Optional[int] = Field(default=None, Primary_key)
    first_name: str
    last_name: str
    middle_name: str
    relationship: Relationship
    student_id: int = Field(foriegn_key="students.id")
