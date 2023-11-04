from rest_framework import serializers
from ..models import Artifact, HistoricalEvents, Sites
from .site import SitesSerializer, StructuresSerializer
from .historical_figure import HistoricalFiguresSerializer
from .written_content import WrittenContentsSerializer
from .historical_figure import HistoricalFiguresSerializer

class HistoricalEventsSerializer(serializers.ModelSerializer):
    hf_id = HistoricalFiguresSerializer()
    target_hfid = HistoricalFiguresSerializer()
    class Meta:
        model = HistoricalEvents
        fields = ['type', 'hf_id', 'target_hfid', 'year']

class ArtifactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = ['name', 'name2', 'item_type', 'id']

class ArtifactSerializer(serializers.ModelSerializer):
    site = SitesSerializer(source='site_id', read_only=True)
    holder = HistoricalFiguresSerializer(source='holder_id', read_only=True)
    wc = WrittenContentsSerializer(source='written_content_id', read_only=True)
    structure = StructuresSerializer(source='structure_id', read_only=True)
    artifact_historical_events = HistoricalEventsSerializer(many=True)
    class Meta:
        model = Artifact
        fields = ['name', 'name2', 'site', 'holder', 'page_number', 'wc', 'item_type', 'material', 'item_subtype', 'item_description', 'structure', 'artifact_historical_events', 'artifact_intrigue_plot']