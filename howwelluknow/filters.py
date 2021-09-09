import django_filters
from .models import *



class HowWellUKnowFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = HowWellUKnow
        fields = '__all__'


class HowWellUKnowScoreFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')
    score = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = HowWellUKnowScore
        fields = '__all__'
