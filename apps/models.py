from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, TextChoices, RESTRICT
from django.utils.text import slugify


class SlugBaseModel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)


class Category(SlugBaseModel):
    pass


class User(AbstractUser):
    class Type(TextChoices):
        ADMIN = 'admin', 'Admin'
        STAFF = 'staff', 'Staff'
        USER = 'user', 'User'

    type = CharField(max_length=10, choices=Type.choices, default=Type.USER)


class Product(SlugBaseModel):
    price = models.IntegerField()
    discount = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('apps.Category', models.CASCADE)
    owner = models.ForeignKey('apps.User', models.SET_NULL, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
