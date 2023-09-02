from typing import List

from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select

from app.database import engine
from app.models.programme import Programme
from app.models.student import Student
from app.serializers.serializers import ProgrammeCreate

router = APIRouter()


@router.post("/programmes/{index_number}",
             tags=["Programmes"],
             response_model=ProgrammeCreate)
def programmes(programme: Programme, index_number: str):
    '''
    Register programme for student
    '''
    with Session(engine) as session:
        try:
            student = session.exec(select(Student).where(
                Student.index_number == index_number)).first()
            if not student:
                raise HTTPException(
                    status_code=404, detail=f'Error: Student with \
                          index number {index_number} not found')

            programme_instance = Programme(
                programme_name=programme.programme_name,
                programme_code=programme.programme_code,
                programme_description=programme.programme_description,
                programme_duration=programme.programme_duration,
                student_id=index_number
            )
            session.add(programme_instance)
            session.commit()
            session.refresh(programme_instance)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return programme_instance


@router.get("/programmes",
            tags=["Programmes"],
            response_model=List[ProgrammeCreate],
            status_code=status.HTTP_200_OK)
def get_programmes():
    '''
    Get all programmes
    '''
    with Session(engine) as session:
        programmes = session.exec(select(Programme)).all()
        return programmes


@router.get("/programmes/by-id/{index_number}",
            tags=["Programmes"],
            response_model=ProgrammeCreate,
            status_code=status.HTTP_200_OK)
def get_programme_by_id(index_number: str):
    '''
    Get programme by student index number
    '''
    with Session(engine) as session:
        try:
            student = session.exec(select(Student).where(
                Student.index_number == index_number)).first()
            if not student:
                raise HTTPException(
                    status_code=404, detail=f'Error: Student with \
                        index number {index_number} not found')

            programme = session.exec(select(Programme).where(
                Programme.student_id == index_number)).first()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return programme


@router.put("/programmes/{index_number}",
            tags=["Programmes"],
            response_model=ProgrammeCreate,
            status_code=status.HTTP_202_ACCEPTED)
def update_programme(index_number: str, programme: ProgrammeCreate):
    '''
    Update programme
    '''
    with Session(engine) as session:
        try:
            programme_instance = session.exec(
                select(Programme).
                where(Programme.student_id == index_number)).first()
            programme_instance.programme_name = programme.programme_name
            programme_instance.programme_code = programme.programme_code
            programme_instance.programme_description = \
                programme.programme_description
            programme_instance.programme_duration = \
                programme.programme_duration
            session.add(programme_instance)
            session.commit()
            session.refresh(programme_instance)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return programme_instance


@router.patch("/programmes/{index_number}",
              tags=["Programmes"],
              response_model=ProgrammeCreate,
              status_code=status.HTTP_200_OK)
def update_programme(programme, index_number: str):
    '''
    Update programme
    '''
    with Session(engine) as session:
        try:
            student = session.exec(select(Student).where(
                Student.index_number == index_number)).first()
            if not student:
                raise HTTPException(
                    status_code=404, detail=f'Error: Student with \
                        index number {index_number} not found')

            programme_instance = session.exec(select(Programme).where(
                Programme.student_id == index_number)).first()
            for key, value in programme.dict().items():
                setattr(programme_instance, key, value)
            session.add(programme_instance)
            session.commit()
            session.refresh(programme_instance)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return programme_instance
