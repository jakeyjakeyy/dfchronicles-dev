from rest_framework import serializers
from ..models import Occasion

class OccasionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occasion
        fields = ['name']