from typing import Union

from fastapi import APIRouter

router = APIRouter()

@router.get("/birds/")
def birds():
    return {"Hello": "World"}


@router.post("/birds/")
def birds(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
