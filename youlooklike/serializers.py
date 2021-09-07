from rest_framework import serializers
from .models import *


class YouLookLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouLookLike
        fields = '__all__'
        
class YouLookLikeScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouLookLikeScore
        fields = '__all__'
        
class YouLookLikeRandomSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouLookLikeRandom
        fields = '__all__'
        
