import uuid
from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from app.enum.relationship import Relationship


class Guardian(SQLModel, table=True):
    __tablename__ = 'guardians'

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(nullable=False, )
    last_name: str = Field(nullable=False, )
    middle_name: str
    relationship: Relationship
    student_id: str = Field(
        foreign_key="students.index_number", unique=True, index=True)
    created_at: Optional[datetime] = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=datetime.now())
