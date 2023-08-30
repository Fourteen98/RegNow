from sqlmodel import Field, SQLModel,
from typing import Optional

class Bird(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str= Field(index=True)
    color: str