from api.crud import comment as comment_crud
from api.crud import user as user_crud
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.factories.comment import CommentFactory
from app.tests.factories.user import UserFactory


def test_create_comment(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    user_in = UserFactory.create()
    user = user_crud.create_with_obj(db, obj_in=user_in)
    data = CommentFactory.create(author_id=user.id)
    r = client.post(
        f"{settings.API_V1_STR}/comments/", headers=superuser_token_headers, json=jsonable_encoder(data),
    )
    assert 200 <= r.status_code < 300
    created_comment = r.json()
    assert created_comment['title'] == data.title


def test_get_comment(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    user_in = UserFactory.create()
    user = user_crud.create_with_obj(db, obj_in=user_in)
    comment_in = CommentFactory.create(author_id=user.id)
    comment = comment_crud.create(db, obj_in=comment_in)
    comment_id = comment.id
    r = client.get(
        f"{settings.API_V1_STR}/comments/{comment_id}", headers=superuser_token_headers,
    )
    assert 200 <= r.status_code < 300
    api_comment = r.json()
    existing_comment = comment_crud.get(db, id=comment_id)
    assert existing_comment
    assert existing_comment.title == api_comment["title"]


def test_update_comment(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    user_in = UserFactory.create()
    user = user_crud.create_with_obj(db, obj_in=user_in)
    comment_in = CommentFactory.create(author_id=user.id)
    created_comment = comment_crud.create(db, obj_in=comment_in)
    created_comment_id = created_comment.id
    new_comment = CommentFactory.create(author_id=user.id)
    data = jsonable_encoder(new_comment)
    r = client.put(
        f"{settings.API_V1_STR}/comments/{created_comment_id}", headers=superuser_token_headers, json=data,
    )
    updated_comment = r.json()
    assert 200 <= r.status_code < 300
    assert updated_comment['id'] == created_comment_id
    assert updated_comment['title'] == new_comment.title


def test_retrieve_comments(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    user_in = UserFactory.create()
    user = user_crud.create_with_obj(db, obj_in=user_in)

    comment_in = CommentFactory.create(author_id=user.id)
    comment_crud.create(db, obj_in=comment_in)

    comment_in = CommentFactory.create(author_id=user.id)
    comment_crud.create(db, obj_in=comment_in)

    r = client.get(f"{settings.API_V1_STR}/comments/",
                   headers=superuser_token_headers)
    all_users = r.json()

    assert len(all_users) > 1
    for item in all_users:
        assert "title" in item
