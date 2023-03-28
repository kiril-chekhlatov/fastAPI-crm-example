from typing import Any, List

import schemas
from api.crud import student as student_crud
from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Student])
def read_students(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
        Retrieve students.
    """
    students = student_crud.get_multi(db, skip=skip, limit=limit)
    return students


@router.post("/", response_model=schemas.Student)
def create_student(
    *,
    db: Session = Depends(get_db),
    student_in: schemas.StudentCreate,
) -> Any:
    """
        Create new student.
    """
    student = student_crud.create(db=db, obj_in=student_in)
    return student


@router.put("/{id}", response_model=schemas.Student)
def update_student(
    *,
    db: Session = Depends(get_db),
    id: int,
    student_in: schemas.StudentUpdate,
) -> Any:
    """
        Update an student.
    """
    student = student_crud.get(db=db, id=id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student = student_crud.update(db=db, db_obj=student, obj_in=student_in)
    return student


@router.get("/{id}", response_model=schemas.Student)
def read_student(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
        Get student by ID.
    """
    student = student_crud.get(db=db, id=id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.delete("/{id}", response_model=schemas.Student)
def delete_student(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
        Delete an student.
        TODO: Можно оптимизировать
    """
    student = student_crud.get(db=db, id=id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student = student_crud.remove(db=db, id=id)
    return student
