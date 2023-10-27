from rest_framework import serializers
from ..models import Identities
from .entity import EntitiesSerializer
from .historical_figure import HistoricalFigureSerializer

class IdentitySerializer(serializers.ModelSerializer):
    entity = EntitiesSerializer(source='civ_id', read_only=True)
    nemesis = HistoricalFigureSerializer(source='nemesis_id', read_only=True)
    class Meta:
        model = Identities
        fields = ['name', 'hf_id', 'birth_year', 'race', 'caste', 'profession', 'entity', 'nemesis']