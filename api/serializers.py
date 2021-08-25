from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        Rating.objects.create(user=user,value=0)
        return user


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuizQuestionBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestionBank
        fields = '__all__'



class RfQuestionBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = RfQuestionBank
        fields = '__all__'


class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entertainment
        fields = '__all__'
        
class EntertainmentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntertainmentResult
        fields = '__all__'
        

class QuizResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResponse
        fields = '__all__'
