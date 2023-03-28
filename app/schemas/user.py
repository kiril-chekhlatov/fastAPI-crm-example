from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel
from schemas import Comment


class UserBase(BaseModel):
    """ Shared properties """
    username: str
    hashed_password: str
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    role: Optional[int] = None
    appointment: Optional[str] = None
    middle_name: Optional[str] = None
    photo: Optional[str] = None
    comments: Optional[List[int]] = []


class UserCreate(UserBase):
    """ Properties to receive on user creation """
    comments: Optional[list] = []


class UserUpdate(UserBase):
    """ Properties to receive on user update """
    pass


class UserInDBBase(UserBase):
    """ Properties shared by models stored in DB """
    id: int
    comments: Optional[List[Comment]] = []
    time_created: datetime
    time_updated: Optional[datetime] = None

    class Config:
        orm_mode = True


class User(UserInDBBase):
    """ Properties to return to client """
    pass


class UserInDB(UserInDBBase):
    """ Properties properties stored in DB """
    pass
