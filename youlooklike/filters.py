import django_filters
from .models import *


class YouLookLikeFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = YouLookLike
        fields = '__all__'


class YouLookLikeResultFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = YouLookLikeResult
        fields = '__all__'

