from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CommentBase(BaseModel):
    """ Shared properties """
    author_id: int
    title: str
    message: str


class CommentCreate(CommentBase):
    """ Properties to receive on сomment creation """
    pass


class CommentUpdate(CommentBase):
    """ Properties to receive on сomment update """
    author_id: int
    title: str
    message: str


class CommentInDBBase(CommentBase):
    """ Properties shared by models stored in DB """
    id: int
    time_created: datetime
    time_updated: Optional[datetime] = None

    class Config:
        orm_mode = True


class Comment(CommentInDBBase):
    """ Properties to return to client """
    pass


class CommentInDB(CommentInDBBase):
    """ Properties properties stored in DB """
    pass
