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



class YouLookLikeFilter(django_filters.FilterSet):
    category = ListFilter(lookup_expr="in")

    class Meta:
        model = YouLookLike
        fields = '__all__'


class YouLookLikeRandomFilter(django_filters.FilterSet):
    category = ListFilter(lookup_expr="in")

    class Meta:
        model = YouLookLikeRandom
        fields = '__all__'


class YouLookLikeScoreFilter(django_filters.FilterSet):
    category = ListFilter(lookup_expr="in")
    code = ListFilter(lookup_expr="in")

    class Meta:
        model = YouLookLikeScore
        fields = '__all__'

