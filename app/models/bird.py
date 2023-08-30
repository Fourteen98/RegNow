from sqlmodel import Field, SQLModel, Column
import uuid

class Bird(SQLModel, table=True):
    __tablename__='birds'
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str= Field(index=True)
    color: str
