from api.crud import region as region_crud
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.factories.region import RegionFactory


def test_create_region(
    client: TestClient, superuser_token_headers: dict
) -> None:
    data = RegionFactory.create()
    r = client.post(
        f"{settings.API_V1_STR}/regions/", headers=superuser_token_headers, json=jsonable_encoder(data),
    )
    assert 200 <= r.status_code < 300
    created_region = r.json()
    assert created_region['name'] == data.name


def test_get_region(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    region_in = RegionFactory.create()
    region = region_crud.create(db, obj_in=region_in)
    region_id = region.id
    r = client.get(
        f"{settings.API_V1_STR}/regions/{region_id}", headers=superuser_token_headers,
    )
    assert 200 <= r.status_code < 300
    api_region = r.json()
    existing_region = region_crud.get(db, id=region_id)
    assert existing_region
    assert existing_region.name == api_region["name"]


def test_update_region(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    region_in = RegionFactory.create()
    created_region = region_crud.create(db, obj_in=region_in)
    created_region_id = created_region.id
    new_name = RegionFactory.create().name
    data = {"name": new_name}
    r = client.put(
        f"{settings.API_V1_STR}/regions/{created_region_id}", headers=superuser_token_headers, json=data,
    )
    updated_region = r.json()
    assert 200 <= r.status_code < 300
    assert updated_region['id'] == created_region_id
    assert updated_region['name'] == new_name


def test_retrieve_regions(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    region_in = RegionFactory.create()
    region_crud.create(db, obj_in=region_in)

    region_in = RegionFactory.create()
    region_crud.create(db, obj_in=region_in)

    r = client.get(f"{settings.API_V1_STR}/regions/",
                   headers=superuser_token_headers)
    all_users = r.json()

    assert len(all_users) > 1
    for item in all_users:
        assert "name" in item
