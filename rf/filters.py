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


class RfQuestionBankFilter(django_filters.FilterSet):
    category = ListFilter(lookup_expr="in")

    class Meta:
        model = RfQuestionBank
        fields = '__all__'


class RfRoomDetailFilter(django_filters.FilterSet):
    category = ListFilter(lookup_expr="in")

    class Meta:
        model = RfRoomDetail
        fields = '__all__'

