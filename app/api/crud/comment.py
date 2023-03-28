from api.crud.base import CRUDBase
from models.comment import Comment
from schemas.comment import CommentCreate, CommentUpdate


class CRUDComment(CRUDBase[Comment, CommentCreate, CommentUpdate]):
    pass


comment = CRUDComment(Comment)
