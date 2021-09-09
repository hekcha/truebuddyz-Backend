from rest_framework import serializers
from .models import *


class RfQuestionBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = RfQuestionBank
        fields = '__all__'

class RfRoomDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RfRoomDetail
        fields = '__all__'

