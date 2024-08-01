from django_filters import FilterSet, NumberFilter

from apps.models import Product


class ProductFilterSet(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = 'category',
