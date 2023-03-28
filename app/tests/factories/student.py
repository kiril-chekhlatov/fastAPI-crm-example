from datetime import date, timedelta

import factory
from factory import fuzzy
from schemas import StudentCreate


class StudentFactory(factory.Factory):
    class Meta:
        model = StudentCreate

    contract_type = fuzzy.FuzzyInteger(
        low=1, high=3)
    name = factory.Faker('name')
    surname = factory.Faker('name')
    middle_name = factory.Faker('name')
    birth_of_date = fuzzy.FuzzyDate(date.today())
    email = factory.Faker('email')
    address = factory.Faker('address')
    phone = '+998919191919'
    passport_series = 'QQ'
    passport_number = fuzzy.FuzzyInteger(low=1)
    PIN = '21312312'
    authority = factory.Faker('address')
    region_id = None
    major_id = None

    gender = fuzzy.FuzzyInteger(low=1, high=4)
    discount = True
    percent = fuzzy.FuzzyFloat(low=1)
    discount_from = fuzzy.FuzzyDate(date.today())
    discount_to = factory.LazyAttribute(
        lambda o: o.discount_from + timedelta(days=2)
    )
    super_contract = True
    super_contract_sum = fuzzy.FuzzyInteger(low=1)
    # comment_id =
    """ passport_document = factory.LazyAttribute(
        lambda _: ContentFile(b'...', name="passport_document.pdf")
    )
    IELTS_document = factory.LazyAttribute(
        lambda _: ContentFile(b'...', name="IELTS_document.pdf")
    ) """
