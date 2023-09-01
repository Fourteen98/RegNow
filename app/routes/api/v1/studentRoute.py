from typing import List

from fastapi import APIRouter, HTTPException, status
from sqlmodel import Session, select
from app.utils.country import Country

from app.database import engine
from app.models.student import Student
from app.models.programme import Programme
from app.models.guardian import Guardian
from app.serializers.serializers import StudentCreate, RegisterStudentCreate

router = APIRouter()


@router.post("/students/", tags=["Students"], response_model=Student)
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
                index_number=Student.generate_index_number(),
            )
            session.add(student_instance)
            session.commit()
            session.refresh(student_instance)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return student_instance


@router.get("/students/", tags=["Students"], response_model=List[Student], status_code=status.HTTP_200_OK)
def read_students():
    with Session(engine) as session:
        students = session.exec(select(Student)).all()
        return students


@router.get("/students/{student_id}", tags=["Students"], response_model=Student, status_code=status.HTTP_200_OK)
def read_student(student_id: int):
    with Session(engine) as session:
        try:
            student = session.exec(select(Student).where(Student.id == student_id)).first()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
        return student


@router.put("/students/{student_id}", tags=["Students"], response_model=Student, status_code=status.HTTP_202_ACCEPTED)
def update_student(student_id: int, student: StudentCreate):
    with Session(engine) as session:
        try:
            student_instance = session.exec(select(Student).where(Student.id == student_id)).first()
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


@router.delete("/students/{student_id}", tags=["Students"], response_model=Student)
def delete_student(student_id: int):
    with Session(engine) as session:
        try:
            student_instance = session.exec(select(Student).where(Student.id == student_id)).first()
            if student_instance:
                session.delete(student_instance)
                session.commit()
            else:
                raise HTTPException(status_code=404, detail=f'Student with ID {student_id} not found')
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=f'Error: {str(e)}')


@router.patch("/students/{student_id}", tags=["Students"], response_model=Student, status_code=status.HTTP_202_ACCEPTED)
def patch_student(student_id: int, student):
    with Session(engine) as session:
        try:
            student_instance = session.exec(select(Student).where(Student.id == student_id)).first()
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

@router.post("/students/register", tags=["Students"], status_code=status.HTTP_201_CREATED)
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
            programme_instance = Programme(
                programme_name=student.programme_name,
                stream=student.stream,
                entry_level=student.entry_level,
                hall=student.hall,
                student_id=student_instance.id
            )
            guardian_instance = Guardian(
                first_name=student.guardian_first_name,
                last_name=student.guardian_last_name,
                middle_name=student.guardian_middle_name,
                relationship=student.guardian_relationship,
                student_id=student_instance.id
            )
            session.add(student_instance)
            session.add(guardian_instance)
            session.add(programme_instance)
            session.refresh(student_instance)
            session.refresh(programme_instance)
            session.refresh(guardian_instance)
            session.commit()
        except Exception as e:
                print(e)
                raise HTTPException(status_code=404, detail=f'Error: {e}')
    return {
        "message": "Student registered successfully",
        "data": {
            "student": student_instance,
            "programme": programme_instance,
            "guardian": guardian_instance
        }
    }

@router.get("/students/register", tags=["Students"], response_model=List[RegisterStudentCreate], status_code=status.HTTP_200_OK)
def read_registered_students():
    with Session(engine) as session:
        print('----> Fetching students full data from all tables')
        try:
            students = session.exec(select(Student, Programme, Guardian).join(Programme).join(Guardian)).all()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=404, detail=f'Error: {e}')
    return students