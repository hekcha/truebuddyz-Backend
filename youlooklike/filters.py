import django_filters
from .models import *



class YouLookLikeFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = YouLookLike
        fields = '__all__'


class YouLookLikeRandomFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = YouLookLikeRandom
        fields = '__all__'


class YouLookLikeScoreFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')
    code = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = YouLookLikeScore
        fields = '__all__'

