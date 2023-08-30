from sqlmodel import SQLModel, Field



class Student(SQLModel, table=True):
    __tablename__ = 'student'
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    middle_name: str
    nationality: str
    age: int
    place_of_birth: str
    current_residence: str
    email: str = Field(unique=True, index=True)
    index_number: str