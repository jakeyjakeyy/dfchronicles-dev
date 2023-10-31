from rest_framework import serializers
from ..models import WrittenContents

class WrittenContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrittenContents
        fields = ['title', 'id']

class WrittenContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrittenContents
        fields = ['title', 'form', 'style', 'source_written_content_reference', 'referenced_written_content_reference', 'written_artifacts']