import pytest
from rest_framework.reverse import reverse_lazy

from apps.models import Product, Category


@pytest.fixture
def category():
    return Category.objects.create(name='Mevalar')
