from typing import List

from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select

from app.database import engine
from app.models.guardian import Guardian
from app.models.programme import Programme
from app.models.student import Student
from app.serializers.serializers import StudentCreate
from app.utils.country import Country

router = APIRouter()


@router.post("/students", tags=["Students"], response_model=Student)
def students(student: StudentCreate):
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
                date_of_birth=student.date_of_birth,
                index_number=Student.generate_index_number(),
            )
            session.add(student_instance)
            session.commit()
            session.refresh(student_instance)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return student_instance


@router.get("/students",
            tags=["Students"],
            response_model=List[Student],
            status_code=status.HTTP_200_OK)
def get_students():
    with Session(engine) as session:
        students = session.exec(select(Student)).all()
        return students


@router.get("/students/{index_number}",
            tags=["Students"],
            response_model=Student,
            status_code=status.HTTP_200_OK)
def get_student(index_number: str):
    with Session(engine) as session:
        try:
            student = session.exec(select(Student).where(
                Student.index_number == index_number)).first()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return student


@router.put("/students/{index_number}",
            tags=["Students"],
            response_model=Student,
            status_code=status.HTTP_202_ACCEPTED)
def update_student(index_number: str, student: StudentCreate):
    with Session(engine) as session:
        try:
            student_instance = session.exec(
                select(Student).
                where(Student.index_number == index_number)).first()
            student_instance.first_name = student.first_name
            student_instance.last_name = student.last_name
            student_instance.middle_name = student.middle_name
            student_instance.gender = student.gender
            student_instance.nationality = Country(student.nationality)
            student_instance.age = student.age
            student_instance.place_of_birth = student.place_of_birth
            student_instance.current_residence = student.current_residence
            student_instance.email = student.email
            session.add(student_instance)
            session.commit()
            session.refresh(student_instance)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return {
            "message": "Student updated successfully",
            "data": student_instance
        }


@router.patch("/students/{index_number}",
              tags=["Students"], response_model=Student,
              status_code=status.HTTP_202_ACCEPTED)
def patch_student(index_number: str, student):
    with Session(engine) as session:
        try:
            student_instance = session.exec(
                select(Student)
                .where(Student.index_number == index_number)).first()
            for key, value in student.dict().items():
                setattr(student_instance, key, value)
            session.add(student_instance)
            session.commit()
            session.refresh(student_instance)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return {
            "message": "Student updated successfully",
            "data": student_instance
        }

@router.delete("/students/{index_number", tags=["Students"], status_code=status.HTTP_204_NO_CONTENT)
def delete_student(index_number: str):
    with Session(engine) as session:
        try:
            student_instance = session.exec(
                select(Student)
                .where(Student.index_number == index_number)).first()
            Guardian.delete_guardian(student_instance.guardian_id)
            Programme.delete_programme(student_instance.programme_id)
            session.delete(student_instance)
            session.commit()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return {
            "message": "Student deleted successfully",
            "data": student_instance
        }