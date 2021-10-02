from rest_framework import serializers
from .models import *

class ThisOrThatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThisOrThat
        fields = '__all__'

class WouldYouRatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WouldYouRather
        fields = '__all__'

