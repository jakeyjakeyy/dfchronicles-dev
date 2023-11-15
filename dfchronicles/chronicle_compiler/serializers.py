from rest_framework import serializers
from .models import Generation

class GenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generation
        fields = '__all__'