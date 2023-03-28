from api.crud import major as major_crud
from api.crud import region as region_crud
from api.crud import student as student_crud
from sqlalchemy.orm import Session

from app.tests.factories.major import MajorFactory
from app.tests.factories.region import RegionFactory
from app.tests.factories.student import StudentFactory


def test_create_student(db: Session) -> None:
    major_in = MajorFactory.create()
    major = major_crud.create(db, obj_in=major_in)
    region_in = RegionFactory.create()
    region = region_crud.create(db, obj_in=region_in)
    student_in = StudentFactory.create(major_id=major.id, region_id=region.id)
    student = student_crud.create(db=db, obj_in=student_in)
    assert student.name == student_in.name


def test_get_student(db: Session) -> None:
    major_in = MajorFactory.create()
    major = major_crud.create(db, obj_in=major_in)
    region_in = RegionFactory.create()
    region = region_crud.create(db, obj_in=region_in)
    student_in = StudentFactory.create(major_id=major.id, region_id=region.id)
    student = student_crud.create(db=db, obj_in=student_in)
    stored_student = student_crud.get(db=db, id=student.id)
    assert stored_student
    assert student.id == stored_student.id
    assert student.name == stored_student.name


def test_update_student(db: Session) -> None:
    major_in = MajorFactory.create()
    major = major_crud.create(db, obj_in=major_in)
    region_in = RegionFactory.create()
    region = region_crud.create(db, obj_in=region_in)
    student_in = StudentFactory.create(major_id=major.id, region_id=region.id)
    student = student_crud.create(db=db, obj_in=student_in)
    student_update = StudentFactory.create(
        major_id=major.id, region_id=region.id)
    student2 = student_crud.update(
        db=db, db_obj=student, obj_in=student_update)
    assert student.id == student2.id
    assert student2.name == student_update.name


def test_delete_student(db: Session) -> None:
    major_in = MajorFactory.create()
    major = major_crud.create(db, obj_in=major_in)
    region_in = RegionFactory.create()
    region = region_crud.create(db, obj_in=region_in)
    student_in = StudentFactory.create(major_id=major.id, region_id=region.id)
    student = student_crud.create(db=db, obj_in=student_in)
    student2 = student_crud.remove(db=db, id=student.id)
    student3 = student_crud.get(db=db, id=student.id)
    assert student3 is None
    assert student2.id == student.id
    assert student2.name == student_in.name
