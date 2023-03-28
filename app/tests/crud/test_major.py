from api.crud import major as crud
from sqlalchemy.orm import Session

from app.tests.factories.major import MajorFactory


def test_create_major(db: Session) -> None:
    major_in = MajorFactory.create()
    major = crud.create(db=db, obj_in=major_in)
    assert major.name == major_in.name


def test_get_major(db: Session) -> None:
    major_in = MajorFactory.create()
    major = crud.create(db=db, obj_in=major_in)
    stored_major = crud.get(db=db, id=major.id)
    assert stored_major
    assert major.id == stored_major.id
    assert major.name == stored_major.name


def test_update_major(db: Session) -> None:
    major_in = MajorFactory.create()
    major = crud.create(db=db, obj_in=major_in)
    major_update = MajorFactory.create()
    major2 = crud.update(db=db, db_obj=major, obj_in=major_update)
    assert major.id == major2.id
    assert major2.name == major_update.name


def test_delete_major(db: Session) -> None:
    major_in = MajorFactory.create()
    major = crud.create(db=db, obj_in=major_in)
    major2 = crud.remove(db=db, id=major.id)
    major3 = crud.get(db=db, id=major.id)
    assert major3 is None
    assert major2.id == major.id
    assert major2.name == major_in.name
