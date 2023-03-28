from typing import Any, List

import schemas
from api.crud import user as user_crud
from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
        Retrieve users.
    """
    users = user_crud.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(get_db),
    user_in: schemas.UserCreate,
) -> Any:
    """
        Create new user.
    """
    user = user_crud.get_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = user_crud.create(db=db, obj_in=user_in)
    return user


@router.put("/{id}", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(get_db),
    id: int,
    user_in: schemas.UserUpdate,
) -> Any:
    """
        Update an user.
    """
    user = user_crud.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = user_crud.update(db=db, db_obj=user, obj_in=user_in)
    return user


@router.get("/{id}", response_model=schemas.User)
def read_user(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
        Get user by ID.
    """
    user = user_crud.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{id}", response_model=schemas.User)
def delete_user(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
        Delete an user.
        TODO: Можно оптимизировать
    """
    user = user_crud.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user = user_crud.remove(db=db, id=id)
    return user
