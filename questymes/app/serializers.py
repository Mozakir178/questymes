from rest_framework import serializers
from .models import Slot


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'
