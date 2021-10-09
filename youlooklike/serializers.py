from rest_framework import serializers
from .models import *


class YouLookLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouLookLike
        fields = '__all__'
    
class YouLookLikeResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouLookLikeResult
        fields = '__all__'
