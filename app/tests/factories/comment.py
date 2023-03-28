import factory
from schemas import CommentCreate


class CommentFactory(factory.Factory):
    class Meta:
        model = CommentCreate

    author_id = None
    title = factory.Sequence(lambda n: 'title %d' % n)
    message = factory.Sequence(lambda n: 'message %d' % n)
