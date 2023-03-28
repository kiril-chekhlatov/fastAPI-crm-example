import random
import string

import factory
from factory import fuzzy
from schemas import UserCreate


def generate_username():
    return random.choice(string.ascii_uppercase) + random.choice(string.digits)


class UserFactory(factory.Factory):
    class Meta:
        model = UserCreate

    name = factory.Sequence(lambda n: 'name %d' % n)
    username = fuzzy.FuzzyAttribute(generate_username)
    hashed_password = factory.Sequence(lambda n: 'password%d' % n)
    is_active = True
    is_superuser = True
    role = fuzzy.FuzzyFloat(low=1)
    appointment = factory.Sequence(lambda n: 'appointment %d' % n)
    middle_name = factory.Sequence(lambda n: 'middle_name %d' % n)
    photo = None
    comments = []
