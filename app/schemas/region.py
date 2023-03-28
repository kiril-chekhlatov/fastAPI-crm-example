from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RegionBase(BaseModel):
    """ Shared properties """
    name: str


class RegionCreate(RegionBase):
    """ Properties to receive on region creation """
    pass


class RegionUpdate(RegionBase):
    """ Properties to receive on major update """
    pass


class RegionInDBBase(RegionBase):
    """ Properties shared by models stored in DB """
    id: int
    time_created: datetime
    time_updated: Optional[datetime] = None

    class Config:
        orm_mode = True


class Region(RegionInDBBase):
    """ Properties to return to client """
    pass


class RegionInDB(RegionInDBBase):
    """ Properties properties stored in DB """
    pass
