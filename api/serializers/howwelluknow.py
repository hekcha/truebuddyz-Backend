from rest_framework import serializers
from ..models.howwelluknow import *
     

class HowWellUKnowSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowWellUKnow
        fields = '__all__'


class HowWellUKnowScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowWellUKnowScore
        fields = '__all__'
