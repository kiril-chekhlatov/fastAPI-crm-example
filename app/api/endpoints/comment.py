from typing import Any, List

import schemas
from api.crud import comment as comment_crud
from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Comment])
def read_comments(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
        Retrieve comments.
    """
    comments = comment_crud.get_multi(db, skip=skip, limit=limit)
    return comments


@router.post("/", response_model=schemas.Comment)
def create_comment(
    *,
    db: Session = Depends(get_db),
    comment_in: schemas.CommentCreate,
) -> Any:
    """
        Create new comment.
    """
    comment = comment_crud.create(db=db, obj_in=comment_in)
    return comment


@router.put("/{id}", response_model=schemas.Comment)
def update_comment(
    *,
    db: Session = Depends(get_db),
    id: int,
    comment_in: schemas.CommentUpdate,
) -> Any:
    """
        Update an comment.
    """
    comment = comment_crud.get(db=db, id=id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    comment = comment_crud.update(db=db, db_obj=comment, obj_in=comment_in)
    return comment


@router.get("/{id}", response_model=schemas.Comment)
def read_comment(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
        Get comment by ID.
    """
    comment = comment_crud.get(db=db, id=id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment


@router.delete("/{id}", response_model=schemas.Comment)
def delete_comment(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
        Delete an comment.
        TODO: Можно оптимизировать
    """
    comment = comment_crud.get(db=db, id=id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    comment = comment_crud.remove(db=db, id=id)
    return comment
