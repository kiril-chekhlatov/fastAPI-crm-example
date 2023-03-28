import factory
from factory import fuzzy
from schemas import MajorCreate


class MajorFactory(factory.Factory):
    class Meta:
        model = MajorCreate

    name = factory.Sequence(lambda n: 'name %d' % n)
    price = fuzzy.FuzzyInteger(low=1)
    description = factory.Sequence(lambda n: 'description %d' % n)
