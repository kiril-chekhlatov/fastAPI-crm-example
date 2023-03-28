from api.crud import user as user_crud
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.factories.user import UserFactory


def test_create_user_new_username(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = UserFactory.create()
    r = client.post(
        f"{settings.API_V1_STR}/users/", headers=superuser_token_headers, json=jsonable_encoder(data),
    )
    print(r.json())
    assert 200 <= r.status_code < 300
    created_user = r.json()
    user = user_crud.get_by_username(db, username=data.username)
    assert user
    assert user.username == created_user["username"]


def test_get_existing_user(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    user_in = UserFactory.create()
    user = user_crud.create_with_obj(db, obj_in=user_in)
    user_id = user.id
    r = client.get(
        f"{settings.API_V1_STR}/users/{user_id}", headers=superuser_token_headers,
    )
    assert 200 <= r.status_code < 300
    api_user = r.json()
    existing_user = user_crud.get_by_username(db, username=user_in.username)
    assert existing_user
    assert existing_user.username == api_user["username"]


def test_create_user_existing_username(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    user_in = UserFactory.create()
    user_crud.create_with_obj(db, obj_in=user_in)
    r = client.post(
        f"{settings.API_V1_STR}/users/", headers=superuser_token_headers, json=jsonable_encoder(user_in),
    )
    created_user = r.json()
    assert r.status_code == 400
    assert "id" not in created_user


def test_retrieve_users(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    user_in = UserFactory.create()
    user_crud.create_with_obj(db, obj_in=user_in)

    user_in2 = UserFactory.create()
    user_crud.create_with_obj(db, obj_in=user_in2)

    r = client.get(f"{settings.API_V1_STR}/users/",
                   headers=superuser_token_headers)
    all_users = r.json()

    assert len(all_users) > 1
    for item in all_users:
        assert "username" in item
