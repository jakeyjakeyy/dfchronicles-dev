from rest_framework import serializers
from ..models import Occasion
from .entity import EntitiesSerializer
from .schedule import SchedulesSerializer

class OccasionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occasion
        fields = ['name', 'id']
        
class OccasionSerializer(serializers.ModelSerializer):
    civ_id = EntitiesSerializer(read_only=True)
    schedules = SchedulesSerializer(source='occasion_schedule.all', many=True, read_only=True)
    class Meta:
        model = Occasion
        fields = ['name', 'civ_id', 'schedules']

        # 'occasion_historical_events'