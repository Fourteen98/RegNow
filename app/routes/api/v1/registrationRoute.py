from typing import List

from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select

from app.database import engine
from app.models.guardian import Guardian
from app.models.programme import Programme
from app.models.student import Student
from app.serializers.serializers import RegisterStudentCreate
from app.utils.country import Country

router = APIRouter()


@router.post("/registrations",
             tags=["Registrations"],
             status_code=status.HTTP_201_CREATED)
def register_student(student: RegisterStudentCreate):
    with Session(engine) as session:
        try:
            student_instance = Student(
                first_name=student.first_name,
                last_name=student.last_name,
                middle_name=student.middle_name,
                gender=student.gender,
                nationality=Country(student.nationality),
                age=student.age,
                place_of_birth=student.place_of_birth,
                current_residence=student.current_residence,
                email=student.email,
                index_number=Student.generate_index_number(),
            )
            session.add(student_instance)
            session.commit()
            session.refresh(student_instance)

            programme_instance = Programme(
                programme_name=student.programme_name,
                stream=student.stream,
                entry_level=student.entry_level,
                hall=student.hall,
                student_id=student_instance.index_number
            )
            session.add(programme_instance)
            session.commit()
            session.refresh(programme_instance)

            guardian_instance = Guardian(
                first_name=student.guardian_first_name,
                last_name=student.guardian_last_name,
                middle_name=student.guardian_middle_name,
                relationship=student.guardian_relationship,
                student_id=student_instance.index_number
            )

            session.add(guardian_instance)
            session.commit()
            session.refresh(guardian_instance)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')

    return {
        'message': "Student registered successfully",
    }


@router.get("/registrations",
            tags=["Registrations"],
            status_code=status.HTTP_200_OK)
def get_registered_students():
    with Session(engine) as session:
        try:
            statement = select(
                Student,
                Programme,
                Guardian).join(
                    Programme,
                    Student.index_number == Programme.student_id).join(
                        Guardian, Student.index_number == Guardian.student_id)
            students = session.exec(statement).all()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')

        return students


@router.get("/students/{index_number}",
            tags=["Students"],
            status_code=status.HTTP_200_OK)
def get_registered_student_by_id(index_number: str):
    with Session(engine) as session:
        try:
            statement = select(Student,
                               Programme,
                               Guardian).join(
                Programme,
                Student.id == Programme.student_id).join(
                Guardian, Student.id == Guardian.student_id).where(
                    Student.index_number == index_number)
            student_instance = session.exec(statement).first()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
    return student_instance


@router.delete("/students/{index_number}",
               tags=["Registrations"],
               status_code=status.HTTP_200_OK)
def delete_student(index_number: str):
    with Session(engine) as session:
        try:
            student_instance = session.exec(
                select(Student)
                .where(Student.index_number == index_number)).first()
            if not student_instance:
                raise HTTPException(
                    status_code=404, detail=f'Student with index number  \
                    {index_number} not found')
            session.delete(student_instance)
            programme_instance = session.exec(
                select(Programme)
                .where(Programme.student_id == index_number)).first()
            session.delete(programme_instance)
            guardian_instance = session.exec(
                select(Guardian)
                .where(Guardian.student_id == index_number)).first()
            session.delete(guardian_instance)
            session.commit()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return {
            "message": "Student deleted successfully",
        }
