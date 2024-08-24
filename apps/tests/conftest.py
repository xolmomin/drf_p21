import pytest

from apps.tests.factories import CategoryFactory, UserFactory


@pytest.fixture
def categories():
    CategoryFactory.create_batch(50)


@pytest.fixture
def users():
    UserFactory.create_batch(50)
