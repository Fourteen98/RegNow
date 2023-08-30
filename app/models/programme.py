import uuid

from sqlmodel import Column, Field, SQLModel


class Program(SQLModel, table=True):
    __tablename__ = 'birds'
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True)
    color: str
