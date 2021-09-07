from rest_framework import serializers
from .models import *


class RfQuestionBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = RfQuestionBank
        fields = '__all__'

