import schemas
from api import crud
from core.config import settings
from sqlalchemy.orm import Session


def init_db(db: Session) -> None:
    user = crud.user.get_by_username(db, username=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            username=settings.FIRST_SUPERUSER,
            hashed_password=settings.FIRST_SUPERUSER_PASSWORD
        )
        user = crud.user.create_with_obj(db, obj_in=user_in)
