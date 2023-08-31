from sqlmodel import SQLModel, Field, DateTime
from datetime import datetime
from sqlalchemy.sql.functions import now

class BaseModel(SQLModel, table=True):
    __tablename__ = 'base_model'
    __abstract__ = True

    created_at: datetime = Field(default=datetime.now(), nullable=False)
    updated_at: datetime = Field(default=datetime.now(), nullable=False)
