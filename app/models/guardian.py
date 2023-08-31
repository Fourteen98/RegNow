import uuid
from sqlmodel import Field, SQLModel, Relationship
from enum import Relationship
from typing import Optional

class Guardian(SQLModel, table=True):
    id int: Optional[int] = Field(default=None, primary_key)
    first_name: str
    last_name: str
    middle_name: str
    relationship: Relationship
    student_id: int = Field(foriegn_key="students.id")
