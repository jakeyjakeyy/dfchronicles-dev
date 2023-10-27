from rest_framework import serializers
from ..models import Landmass

class LandmassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landmass
        fields = ['name', 'coord1', 'coord2']