from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MajorBase(BaseModel):
    """ Shared properties """
    name: str
    price: int
    description: str


class MajorCreate(MajorBase):
    """ Properties to receive on major creation """
    pass


class MajorUpdate(MajorBase):
    """ Properties to receive on major update """
    pass


class MajorInDBBase(MajorBase):
    """ Properties shared by models stored in DB """
    id: int
    time_created: datetime
    time_updated: Optional[datetime] = None

    class Config:
        orm_mode = True


class Major(MajorInDBBase):
    """ Properties to return to client """
    pass


class MajorInDB(MajorInDBBase):
    """ Properties properties stored in DB """
    pass
