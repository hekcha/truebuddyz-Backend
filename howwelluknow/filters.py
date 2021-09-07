import django_filters
from django_filters.constants import EMPTY_VALUES
from .models import *


class ListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        value_list = value.split(",")
        qs = super().filter(qs, value_list)
        return qs


class HowWellUKnowFilter(django_filters.FilterSet):
    category = ListFilter(lookup_expr="in")

    class Meta:
        model = HowWellUKnow
        fields = '__all__'


class HowWellUKnowScoreFilter(django_filters.FilterSet):
    category = ListFilter(lookup_expr="in")
    score = ListFilter(lookup_expr="in")

    class Meta:
        model = HowWellUKnowScore
        fields = '__all__'
