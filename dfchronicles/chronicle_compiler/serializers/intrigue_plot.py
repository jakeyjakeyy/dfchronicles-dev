from rest_framework import serializers
from ..models import IntriguePlot

class IntriguePlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntriguePlot
        fields = ['type']