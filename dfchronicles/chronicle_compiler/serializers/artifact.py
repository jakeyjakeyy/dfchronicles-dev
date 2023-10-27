from rest_framework import serializers
from ..models import Artifact
from .site import SitesSerializer, StructuresSerializer
from .historical_figure import HistoricalFiguresSerializer
from .written_content import WrittenContentsSerializer
from .historical_event import HistoricalEventsSerializer

class ArtifactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ['name', 'name2', 'item_type', 'id'] 
class ArtifactSerializer(serializers.ModelSerializer):
    site = SitesSerializer(source='site_id', read_only=True)
    holder = HistoricalFiguresSerializer(source='holder_id', read_only=True)
    wc = WrittenContentsSerializer(source='written_content_id', read_only=True)
    structure = StructuresSerializer(source='structure_id', read_only=True)
    events = HistoricalEventsSerializer(source='artifact_historical_events', many=True, read_only=True)
    class Meta:
        model = Artifact
        fields = ['name', 'name2', 'site', 'holder', 'page_number', 'wc', 'item_type', 'material', 'item_subtype', 'item_description', 'structure', 'events', 'artifact_intrigue_plot']