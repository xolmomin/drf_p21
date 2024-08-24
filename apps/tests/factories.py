import factory

from apps.models import Category, User


class CategoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('company')

    class Meta:
        model = Category


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.LazyAttribute(lambda a: '{}_{}'.format(a.first_name, a.last_name).lower())
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = factory.django.Password('1')
    date_joined = factory.Faker('date_time')
    type = factory.Iterator(list(zip(*User.Type.choices))[0])

    # date_joined = factory.LazyFunction(datetime.datetime.now)

    # username = LazyAttribute(lambda i: ''.join(Faker('words')))

    class Meta:
        model = User
