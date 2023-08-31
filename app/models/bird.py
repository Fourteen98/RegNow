from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Bird(SQLModel, table=True):
    __tablename__ = 'birds'

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=50, nullable=False)
    color: str
    created_at: Optional[datetime] = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=datetime.now())
