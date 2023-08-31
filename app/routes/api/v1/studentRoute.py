from typing import List

from fastapi import APIRouter
from sqlmodel import Session, select

from app.database import engine
from app.models.student import Student
from app.serializers.serializers import StudentCreate

router = APIRouter()


@router.post("/students/")
def students(student: StudentCreate):
    with Session(engine) as session:
        student_instance = Student(**student.dict())
        session.add(student_instance)
        session.commit()
        session.refresh(student_instance)
        return student_instance
