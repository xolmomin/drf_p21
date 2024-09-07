from rest_framework.routers import DefaultRouter

from apps.views import (
    CategoryListCreateAPIView,
    ProductListCreateAPIView,
    RegisterCreateAPIView,
    UserListAPIView, ProductDocumentViewSet,
)
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('products', ProductDocumentViewSet, 'products')

urlpatterns = [
    path('', include(router.urls)),
    path('users', UserListAPIView.as_view(), name='users'),
    path('categories', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('products-postgres', ProductListCreateAPIView.as_view(), name='product-list'),
    path('auth/register', RegisterCreateAPIView.as_view(), name='register'),
    path('token', obtain_auth_token, name='token_obtain_pair'),
    # path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
