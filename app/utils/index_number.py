from sqlmodel import Session
from app.database import engine
from app.models.student import Student


class IndexNumber():
    index_base: str = 'B'
    def __init__(self) -> None:
        self.index_number = self.generate_index_number()

    def generate_index_number(self) -> str:
        with Session(engine) as session:
            # get the last record
            
        return self.index_base + str(self.get_index_number())