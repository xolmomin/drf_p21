from django.db.models import QuerySet, IntegerChoices
from django.db.models.functions import Length
from django_filters import FilterSet, NumberFilter, ChoiceFilter

from apps.models import Product, User


class ProductFilterSet(FilterSet):
    class Number(IntegerChoices):
        N1 = 1
        N2 = 2
        N3 = 3

    n = ChoiceFilter(choices=Number.choices)

    class Meta:
        model = Product
        fields = 'category',

    # def get_length(self, queryset, name, value):
    #     return queryset.annotate(name_length=Length('name')).filter(name_length__gte=value)


# categoryni filter qilish, productlar soniga qarab
# product filter image bor yoki yoqligiga qarab
# product filter  3, 7, 10, 15 oxirgi yaratilgan productlarni

