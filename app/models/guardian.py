import uuid
from sqlmodel import Field, SQLModel, Relationship
from enum import Relationship


class Guardian(SQLModel, table=True):
    int: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    first_name: str
    last_name: str
    middle_name: str
    relationship: Relationship
    student_id: int = Field(foriegn_key="student.id")

    student = Relationship("Student", back_populates="guardians")
