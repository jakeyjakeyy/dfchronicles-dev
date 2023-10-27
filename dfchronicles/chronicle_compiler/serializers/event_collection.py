from rest_framework import serializers
from ..models import HistoricalEventCollections

class EventCollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalEventCollections
        fields = ['name', 'type']