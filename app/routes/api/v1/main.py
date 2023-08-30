from typing import List

from fastapi import APIRouter
from sqlmodel import Session, select

from app.database import engine
from app.models.bird import Bird

router = APIRouter()


@router.get("/birds/", response_model=List[Bird])
def birds():
    with Session(engine) as session:
        query = select(Bird)
        birds = session.exec(query).all()
    return birds


@router.post("/birds/")
def birds(bird: Bird):
    with Session(engine) as session:
        session.add(bird)
        session.commit()
        session.refresh(bird)
        return bird
