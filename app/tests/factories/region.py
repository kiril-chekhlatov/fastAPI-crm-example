import factory
from schemas import RegionCreate


class RegionFactory(factory.Factory):
    class Meta:
        model = RegionCreate

    name = factory.Sequence(lambda n: 'name %d' % n)
