from typing import List

from fastapi import APIRouter
from sqlmodel import Session, select

from app.database import engine
from app.models.bird import Bird
from app.serializers.serializers import BirdCreate

router = APIRouter()


@router.get("/birds/", response_model=List[Bird])
def birds():
    with Session(engine) as session:
        query = select(Bird)
        birds = session.exec(query).all()
    return birds


@router.post("/birds/")
def birds(bird: BirdCreate):
    with Session(engine) as session:
        bird_instance = Bird(**bird.dict())
        session.add(bird_instance)
        session.commit()
        session.refresh(bird_instance)
        return bird_instance
