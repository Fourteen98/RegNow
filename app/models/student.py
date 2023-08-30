from sqlmodel import SQLModel, Field, Column
import uuid


class Student(SQLModel, table=True):
    __tablename__ = 'students'
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str
    last_name: str
    middle_name: str
    nationality: str
    age: int
    place_of_birth: str
    current_residence: str
    email: str = Field(unique=True, index=True)
    index_number: str
