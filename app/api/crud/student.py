from typing import List

from api.crud.base import CRUDBase
from fastapi.encoders import jsonable_encoder
from models.student import Student
from schemas.student import StudentCreate, StudentUpdate
from sqlalchemy.orm import Session


class CRUDStudent(CRUDBase[Student, StudentCreate, StudentUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: StudentCreate, owner_id: int
    ) -> Student:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Student]:
        return (
            db.query(self.model)
            .filter(Student.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


student = CRUDStudent(Student)
