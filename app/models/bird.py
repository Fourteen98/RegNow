import uuid
from sqlmodel import Field, SQLModel

# Gender as tuple
class Bird(SQLModel, table=True):
    __tablename__ = 'birds'

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False)
    name: str = Field(index=True, max_length=50, nullable=False)
    color: str
