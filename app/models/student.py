import uuid
from datetime import datetime, date
from typing import Optional

from pydantic import EmailStr
from sqlmodel import Field, Session, SQLModel, select

from app.database import engine
from app.enum import Gender
from app.utils.country import Country


class Student(SQLModel, table=True):
    __tablename__ = 'students'

    id: Optional[int] = Field(default_factory=None, primary_key=True)
    first_name: str
    last_name: str
    middle_name: str
    gender: Gender
    nationality: Country
    age: int
    place_of_birth: str
    current_residence: str
    email: EmailStr
    date_of_birth: date
    index_number: Optional[str] = Field(
        default=None, index=True)
    created_at: Optional[datetime] = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=datetime.now())

    @classmethod
    def generate_index_number(cls) -> str:
        index_base: str = 'B202210100'  # Starting base index number
        with Session(engine) as session:
            query = session.execute(select(cls).order_by(
                cls.id.desc()).limit(1))

            last_index_field = query.scalar()
            if last_index_field:
                last_index_number = int(
                    str(last_index_field.index_number)[-3:]) + 1
            else:
                last_index_number = '001'
            new_index_field = f"{index_base[:-3]}{last_index_number}"
        return new_index_field
