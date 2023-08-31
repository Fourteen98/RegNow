from sqlmodel import SQLModel, Field
import uuid
from pydantic import EmailStr
from app.models.base_model import BaseModel
from app.enum import Gender
from app.utils.country import Country


class Student(SQLModel, table=True):
    __tablename__ = 'students'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
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
