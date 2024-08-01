from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView

from apps.filters import ProductFilterSet
from apps.models import Category, Product
from apps.serializers import CategoryModelSerializer, ProductModelSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = DjangoFilterBackend, SearchFilter, OrderingFilter
    # filterset_fields = 'category',
    filterset_class = ProductFilterSet
    search_fields = 'name', 'description'
    ordering_fields = 'created_at', 'price'
