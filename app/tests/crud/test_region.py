from api.crud import region as crud
from sqlalchemy.orm import Session

from app.tests.factories.region import RegionFactory


def test_create_region(db: Session) -> None:
    region_in = RegionFactory.create()
    region = crud.create(db=db, obj_in=region_in)
    assert region.name == region_in.name


def test_get_region(db: Session) -> None:
    region_in = RegionFactory.create()
    region = crud.create(db=db, obj_in=region_in)
    stored_region = crud.get(db=db, id=region.id)
    assert stored_region
    assert region.id == stored_region.id
    assert region.name == stored_region.name


def test_update_region(db: Session) -> None:
    region_in = RegionFactory.create()
    region = crud.create(db=db, obj_in=region_in)
    region_update = RegionFactory.create()
    region2 = crud.update(db=db, db_obj=region, obj_in=region_update)
    assert region.id == region2.id
    assert region2.name == region_update.name


def test_delete_region(db: Session) -> None:
    region_in = RegionFactory.create()
    region = crud.create(db=db, obj_in=region_in)
    region2 = crud.remove(db=db, id=region.id)
    region3 = crud.get(db=db, id=region.id)
    assert region3 is None
    assert region2.id == region.id
    assert region2.name == region_in.name
