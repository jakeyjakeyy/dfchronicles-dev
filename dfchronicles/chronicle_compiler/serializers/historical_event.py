from rest_framework import serializers
from ..models import HistoricalEvents

class HistoricalEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalEvents
        fields = ['type']