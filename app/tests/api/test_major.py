from api.crud import major as major_crud
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.factories.major import MajorFactory


def test_create_major(
    client: TestClient, superuser_token_headers: dict
) -> None:
    data = MajorFactory.create()
    r = client.post(
        f"{settings.API_V1_STR}/majors/", headers=superuser_token_headers, json=jsonable_encoder(data),
    )
    assert 200 <= r.status_code < 300
    created_major = r.json()
    assert created_major['name'] == data.name


def test_get_major(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    major_in = MajorFactory.create()
    major = major_crud.create(db, obj_in=major_in)
    major_id = major.id
    r = client.get(
        f"{settings.API_V1_STR}/majors/{major_id}", headers=superuser_token_headers,
    )
    assert 200 <= r.status_code < 300
    api_major = r.json()
    existing_major = major_crud.get(db, id=major_id)
    assert existing_major
    assert existing_major.name == api_major["name"]


def test_update_major(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    major_in = MajorFactory.create()
    created_major = major_crud.create(db, obj_in=major_in)
    created_major_id = created_major.id
    data = MajorFactory.create()
    r = client.put(
        f"{settings.API_V1_STR}/majors/{created_major_id}", headers=superuser_token_headers, json=jsonable_encoder(data),
    )
    updated_major = r.json()
    assert 200 <= r.status_code < 300
    assert updated_major['id'] == created_major_id
    assert updated_major['name'] == data.name


def test_retrieve_majors(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    major_in = MajorFactory.create()
    major_crud.create(db, obj_in=major_in)

    major_in = MajorFactory.create()
    major_crud.create(db, obj_in=major_in)

    r = client.get(f"{settings.API_V1_STR}/majors/",
                   headers=superuser_token_headers)
    all_users = r.json()

    assert len(all_users) > 1
    for item in all_users:
        assert "name" in item
