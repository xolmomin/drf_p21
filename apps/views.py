from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.filters import ProductFilterSet
from apps.models import Category, Product, User
from apps.serializers import CategoryModelSerializer, ProductModelSerializer, RegisterUserModelSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = DjangoFilterBackend, SearchFilter, OrderingFilter
    # filterset_fields = 'category',
    permission_classes = AllowAny,
    filterset_class = ProductFilterSet
    search_fields = 'name', 'description'
    ordering_fields = 'created_at', 'price'


class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserModelSerializer
    permission_classes = AllowAny,
