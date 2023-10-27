from rest_framework import serializers
from ..models import HistoricalEras

class ErasSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalEras
        fields = ['name', 'start_year', 'end_year']