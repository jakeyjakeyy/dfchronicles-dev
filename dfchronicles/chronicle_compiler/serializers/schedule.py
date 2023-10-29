from ..models import *
from rest_framework import serializers


class FeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['type']

class SchedulesSerializer(serializers.ModelSerializer):
    schedule_feature = FeaturesSerializer(many=True, read_only=True)
    class Meta:
        model = Schedule
        fields = ['id', 'type', 'item_type', 'item_subtype', 'occasion_schedule_id', 'schedule_feature']