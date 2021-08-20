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


class QuizFilter(django_filters.FilterSet):
    quizcode = ListFilter(lookup_expr="in")

    class Meta:
        model = Quiz
        fields = '__all__'


class QuizResponseFilter(django_filters.FilterSet):
    code = ListFilter(lookup_expr="in")

    class Meta:
        model = QuizResponse
        fields = '__all__'

class QuizQuestionBankFilter(django_filters.FilterSet):
    category = ListFilter(lookup_expr="in")

    class Meta:
        model = QuizQuestionBank
        fields = '__all__'

class RfQuestionBankFilter(django_filters.FilterSet):
    category = ListFilter(lookup_expr="in")

    class Meta:
        model = RfQuestionBank
        fields = '__all__'
