import uuid
from datetime import datetime
from typing import Optional

from pydantic import EmailStr
from sqlmodel import Field, SQLModel, Session, select

from app.enum import Gender
from app.utils.country import Country
from app.database import engine


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
    index_number: Optional[str] = Field(
        default=None, index=True)
    created_at: Optional[datetime] = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=datetime.now())



    @classmethod
    def generate_index_number(cls) -> str:
        index_base: str = 'B202210100'  # Starting base index number
        with Session(engine) as session:
            # Check if there are any records in the database
            query = session.execute(select(cls).order_by(
                cls.id.desc()).limit(1))

            last_index_field = query.scalar()
            if last_index_field:
                # If a record exists, extract the last 3 digits and increment
                print('---> last_index_field: ', last_index_field)
                last_index_number = int(str(last_index_field.index_number)[-3:]) + 1
            else:
                # If no records exist, start from 1
                last_index_number = '001'
            new_index_field = f"{index_base[:-3]}{last_index_number}"
        print('---> new_index_field: ', new_index_field)
        return new_index_field