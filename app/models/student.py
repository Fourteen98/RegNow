import uuid
from typing import Optional

from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from app.enum import Gender
from app.utils.country import Country


class Student(SQLModel, table=True):
    __tablename__ = 'students'

    id: Optional[int] = Field(default_factory=None, primary_key=True)
    first_name: str
    last_name: str
    middle_name: str
    gender: Gender
    nationality: Country
    age: int
    place_of_birth: str
    current_residence: str
    email: EmailStr
    index_number: str
