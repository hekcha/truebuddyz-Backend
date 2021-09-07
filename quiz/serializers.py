from rest_framework import serializers
from .models import *
     

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuizQuestionBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestionBank
        fields = '__all__'


class QuizResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResponse
        fields = '__all__'
