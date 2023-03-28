from typing import Any, List

import schemas
from api.crud import major as major_crud
from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Major])
def read_majors(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
        Retrieve majors.
    """
    majors = major_crud.get_multi(db, skip=skip, limit=limit)
    return majors


@router.post("/", response_model=schemas.Major)
def create_major(
    *,
    db: Session = Depends(get_db),
    major_in: schemas.MajorCreate,
) -> Any:
    """
        Create new region.
    """
    region = major_crud.create(db=db, obj_in=major_in)
    return region


@router.put("/{id}", response_model=schemas.Major)
def update_major(
    *,
    db: Session = Depends(get_db),
    id: int,
    major_in: schemas.MajorUpdate,
) -> Any:
    """
        Update an major.
    """
    major = major_crud.get(db=db, id=id)
    if not major:
        raise HTTPException(status_code=404, detail="Major not found")
    major = major_crud.update(db=db, db_obj=major, obj_in=major_in)
    return major


@router.get("/{id}", response_model=schemas.Major)
def read_major(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
        Get major by ID.
    """
    major = major_crud.get(db=db, id=id)
    if not major:
        raise HTTPException(status_code=404, detail="Major not found")
    return major


@router.delete("/{id}", response_model=schemas.Major)
def delete_major(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
        Delete an major.
        TODO: Можно оптимизировать
    """
    major = major_crud.get(db=db, id=id)
    if not major:
        raise HTTPException(status_code=404, detail="Major not found")
    major = major_crud.remove(db=db, id=id)
    return major
