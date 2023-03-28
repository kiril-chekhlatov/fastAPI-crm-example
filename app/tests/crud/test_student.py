from api.crud import comment as crud
from api.crud import user as user_crud
from sqlalchemy.orm import Session

from app.tests.factories.comment import CommentFactory
from app.tests.factories.user import UserFactory


def test_create_comment(db: Session) -> None:
    user_in = UserFactory.create()
    user = user_crud.create_with_obj(db, obj_in=user_in)
    comment_in = CommentFactory.create(author_id=user.id)
    comment = crud.create(db=db, obj_in=comment_in)
    assert comment.title == comment_in.title


def test_get_comment(db: Session) -> None:
    user_in = UserFactory.create()
    user = user_crud.create_with_obj(db, obj_in=user_in)
    comment_in = CommentFactory.create(author_id=user.id)
    comment = crud.create(db=db, obj_in=comment_in)
    stored_comment = crud.get(db=db, id=comment.id)
    assert stored_comment
    assert comment.id == stored_comment.id
    assert comment.title == stored_comment.title


def test_update_comment(db: Session) -> None:
    user_in = UserFactory.create()
    user = user_crud.create_with_obj(db, obj_in=user_in)
    comment_in = CommentFactory.create(author_id=user.id)
    comment = crud.create(db=db, obj_in=comment_in)
    comment_update = CommentFactory.create(author_id=user.id)
    comment2 = crud.update(db=db, db_obj=comment, obj_in=comment_update)
    assert comment.id == comment2.id
    assert comment2.title == comment_update.title


def test_delete_comment(db: Session) -> None:
    user_in = UserFactory.create()
    user = user_crud.create_with_obj(db, obj_in=user_in)
    comment_in = CommentFactory.create(author_id=user.id)
    comment = crud.create(db=db, obj_in=comment_in)
    comment2 = crud.remove(db=db, id=comment.id)
    comment3 = crud.get(db=db, id=comment.id)
    assert comment3 is None
    assert comment2.id == comment.id
    assert comment2.title == comment_in.title
