import pytest
from rest_framework import status
from rest_framework.reverse import reverse_lazy


@pytest.mark.django_db
class TestView:
    def test_category(self, client, category):
        url = reverse_lazy('category-list')
        response = client.get(url)
        data = response.json()
        assert response.status_code == status.HTTP_200_OK
        assert len(data) == 1
        assert data[0]['id'] == category.id
        assert data[0]['name'] == category.name

    def test_product(self, client, category):
        url = reverse_lazy('product-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN
