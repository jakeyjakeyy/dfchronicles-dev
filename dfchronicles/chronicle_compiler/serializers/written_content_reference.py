from rest_framework import serializers
from ..models import WrittenContentReference
from .written_content import WrittenContentsSerializer
from .site import SitesSerializer

class WrittenContentReferenceSerializer(serializers.ModelSerializer):
    written_content = WrittenContentsSerializer(read_only=True)
    written_content_reference = WrittenContentsSerializer(read_only=True)
    site = SitesSerializer(read_only=True)
    class Meta:
        model = WrittenContentReference
        fields = ['musical_form', 'poetic_form', 'dance_form', 'site', 'written_content_reference']