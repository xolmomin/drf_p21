from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import SlugField

from apps.models import Category, Product


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'first_name', 'last_name', 'username'


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name', 'slug'
        read_only_fields = 'slug',


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = 'updated_at',
        read_only_fields = 'slug',

    def to_representation(self, instance: Product):
        repr = super().to_representation(instance)
        repr['category'] = CategoryModelSerializer(instance.category).data
        return repr
