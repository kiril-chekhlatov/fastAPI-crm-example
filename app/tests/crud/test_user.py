from api.crud import user as crud
from core.security import verify_password
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.tests.factories.user import UserFactory


def test_create_user(db: Session) -> None:
    user_in = UserFactory.create()
    user = crud.create_with_obj(db, obj_in=user_in)
    assert user.username == user_in.username
    assert hasattr(user, "hashed_password")


def test_authenticate_user(db: Session) -> None:
    user_in = UserFactory.create()
    user = crud.create_with_obj(db, obj_in=user_in)
    authenticated_user = crud.authenticate(
        db, username=user_in.username, password=user_in.hashed_password)
    assert authenticated_user
    assert user.username == authenticated_user.username


def test_not_authenticate_user(db: Session) -> None:
    user = UserFactory.create()
    user = crud.authenticate(db, username=user.username,
                             password=user.hashed_password)
    assert user is None


def test_check_if_user_is_active(db: Session) -> None:
    user_in = UserFactory.create()
    user = crud.create_with_obj(db, obj_in=user_in)
    is_active = crud.is_active(user)
    assert is_active is True


def test_check_if_user_is_active_inactive(db: Session) -> None:
    user_in = UserFactory.create()
    user = crud.create_with_obj(db, obj_in=user_in)
    is_active = crud.is_active(user)
    assert is_active


def test_check_if_user_is_superuser(db: Session) -> None:
    user_in = UserFactory.create()
    user = crud.create_with_obj(db, obj_in=user_in)
    is_superuser = crud.is_superuser(user)
    assert is_superuser is True


def test_get_user(db: Session) -> None:
    user_in = UserFactory.create()
    user = crud.create_with_obj(db, obj_in=user_in)
    user_2 = crud.get(db, id=user.id)
    assert user_2
    assert user.username == user_2.username
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


def test_update_user(db: Session) -> None:
    user_in = UserFactory.create()
    user = crud.create_with_obj(db, obj_in=user_in)
    user_in_update = UserFactory.create()
    crud.update(db, db_obj=user, obj_in=user_in_update)
    user_2 = crud.get(db, id=user.id)
    assert user_2
    assert user.username == user_2.username
    assert verify_password(
        user_in_update.hashed_password, user_2.hashed_password)
