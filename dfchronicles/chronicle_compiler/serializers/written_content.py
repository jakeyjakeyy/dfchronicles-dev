from rest_framework import serializers
from ..models import WrittenContents

class WrittenContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrittenContents
        fields = ['title', 'form']