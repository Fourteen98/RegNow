from sqlmodel import SQLModel, Relationship
from app.models.students import Student


class Programme(SQLModel, table=True):
    __tablename__ = "programmmes"

    programme_name: str
    stream: str
    entry_level: str
    hall: str
    student: Student = Relationship(
        back_populates="students", link_model=Student)
