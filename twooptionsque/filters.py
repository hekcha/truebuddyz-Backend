import django_filters
from .models import *

class ThisOrThatFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = ThisOrThat
        fields = '__all__'

class WouldYouRatherFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = WouldYouRather
        fields = '__all__'
