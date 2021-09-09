import django_filters
from .models import *



class QuizFilter(django_filters.FilterSet):
    quizcode = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Quiz
        fields = '__all__'


class QuizResponseFilter(django_filters.FilterSet):
    code = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = QuizResponse
        fields = '__all__'


class QuizQuestionBankFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = QuizQuestionBank
        fields = '__all__'

