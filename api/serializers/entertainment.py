from rest_framework import serializers
from ..models.entertainment import *


class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entertainment
        fields = '__all__'
        
class EntertainmentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntertainmentResult
        fields = '__all__'
        
