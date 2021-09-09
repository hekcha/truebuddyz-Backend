import django_filters
from .models import *


class RfQuestionBankFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = RfQuestionBank
        fields = '__all__'


class RfRoomDetailFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = RfRoomDetail
        fields = '__all__'

