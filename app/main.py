from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routes.api.v1 import main

app = FastAPI()

app.include_router(main.router, prefix="/api/v1")

@app.on_event("startup")
def startup():
    create_db_and_tables()
