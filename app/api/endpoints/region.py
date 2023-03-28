from typing import Any, List

import schemas
from api.crud import region as region_crud
from api.deps import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=List[schemas.Region])
def read_regions(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
        Retrieve regions.
    """
    regions = region_crud.get_multi(db, skip=skip, limit=limit)
    return regions


@router.post("/", response_model=schemas.Region)
def create_region(
    *,
    db: Session = Depends(get_db),
    region_in: schemas.RegionCreate,
) -> Any:
    """
        Create new region.
    """
    region = region_crud.create(db=db, obj_in=region_in)
    return region


@router.put("/{id}", response_model=schemas.Region)
def update_region(
    *,
    db: Session = Depends(get_db),
    id: int,
    region_in: schemas.RegionUpdate,
) -> Any:
    """
        Update an region.
    """
    region = region_crud.get(db=db, id=id)
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    region = region_crud.update(db=db, db_obj=region, obj_in=region_in)
    return region


@router.get("/{id}", response_model=schemas.Region)
def read_region(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
        Get region by ID.
    """
    region = region_crud.get(db=db, id=id)
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    return region


@router.delete("/{id}", response_model=schemas.Region)
def delete_region(
    *,
    db: Session = Depends(get_db),
    id: int,
) -> Any:
    """
        Delete an region.
        TODO: Можно оптимизировать
    """
    region = region_crud.get(db=db, id=id)
    if not region:
        raise HTTPException(status_code=404, detail="Region not found")
    region = region_crud.remove(db=db, id=id)
    return region
