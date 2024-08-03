from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.views import CategoryListCreateAPIView, ProductListCreateAPIView, RegisterCreateAPIView

urlpatterns = [
    path('categories', CategoryListCreateAPIView.as_view()),
    path('products', ProductListCreateAPIView.as_view()),
    path('register', RegisterCreateAPIView.as_view(), name='register_view'),
    path('token', obtain_auth_token, name='token_obtain_pair'),
    # path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
