from rest_framework import serializers
from ..models import MountainPeak

class MountainPeaksSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountainPeak
        fields = ['name', 'height', 'volcano']