from typing import List

from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select

from app.database import engine
from app.models.guardian import Guardian
from app.models.student import Student
from app.serializers.serializers import GuardianCreate

router = APIRouter()


@router.post("/guardian/{index_number}",
             tags=["Guardians"],
             response_model=GuardianCreate)
def guardians(guardian: Guardian, index_number: str):
    with Session(engine) as session:
        try:
            student = session.exec(select(Student).where(
                Student.index_number == index_number)).first()
            if not student:
                raise HTTPException(
                    status_code=404,
                    detail=f'Error: Student with index number \
                        {index_number} not found')

            guardian_instance = Guardian(
                first_name=guardian.first_name,
                last_name=guardian.last_name,
                middle_name=guardian.middle_name,
                relationship=guardian.relationship,
                student_id=index_number
            )
            session.add(guardian_instance)
            session.commit()
            session.refresh(guardian_instance)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return guardian_instance


@router.get("/guardians", tags=["Guardians"],
            response_model=List[GuardianCreate],
            status_code=status.HTTP_200_OK)
def get_guardians():
    with Session(engine) as session:
        guardians = session.exec(select(Guardian)).all()
        return guardians


@router.get("/guardians/by-id/{index_number}",
            tags=["Guardians"],
            response_model=GuardianCreate,
            status_code=status.HTTP_200_OK)
def get_guardian_by_id(index_number: str):
    with Session(engine) as session:
        try:
            student = session.exec(select(Student).where(
                Student.index_number == index_number)).first()
            if not student:
                raise HTTPException(
                    status_code=404, detail=f'Error: Student with \
                          index number \
                    {index_number} not found')

            guardian = session.exec(select(Guardian).where(
                Guardian.student_id == index_number)).first()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return guardian


@router.patch("/guardians/{index_number}",
              tags=["Guardians"],
              response_model=GuardianCreate,
              status_code=status.HTTP_200_OK)
def update_guardian(guardian, index_number: str):
    with Session(engine) as session:
        try:
            student = session.exec(select(Student).where(
                Student.index_number == index_number)).first()
            if not student:
                raise HTTPException(
                    status_code=404, detail=f'Error: Student with \
                        index number {index_number} not found')

            guardian_instance = session.exec(select(Guardian).where(
                Guardian.student_id == index_number)).first()
            guardian_instance.first_name = guardian.first_name
            guardian_instance.last_name = guardian.last_name
            guardian_instance.middle_name = guardian.middle_name
            guardian_instance.relationship = guardian.relationship

            session.add(guardian_instance)
            session.commit()
            session.refresh(guardian_instance)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return guardian_instance


@router.put("/guardians/{index_number}",
            tags=["Guardians"],
            response_model=GuardianCreate,
            status_code=status.HTTP_200_OK)
def update_guardian(guardian: Guardian, index_number: str):
    with Session(engine) as session:
        try:
            student = session.exec(select(Student).where(
                Student.index_number == index_number)).first()
            if not student:
                raise HTTPException(
                    status_code=404, detail=f'Error: Student with \
                    index number {index_number} not found')

            guardian_instance = session.exec(select(Guardian).where(
                Guardian.student_id == index_number)).first()
            for key, value in guardian.dict().items():
                setattr(guardian_instance, key, value)

            session.add(guardian_instance)
            session.commit()
            session.refresh(guardian_instance)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return guardian_instance
