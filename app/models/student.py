from sqlmodel import SQLModel, Field, Relationship, List

from .enums import Nationality, Gender

import uuid

from .programme import Programme


class Student(SQLModel, table=True):
    __tablename__ = 'students'
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str
    last_name: str
    middle_name: str
    nationality: Nationality
    gender: Gender
    age: int
    place_of_birth: str
    current_residence: str
    email: str = Field(unique=True, index=True)
    index_number: str

    programme: List[Programme] = Relationship(back_populates="students")
