from rest_framework import serializers
from .models import Generation

class GenerationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Generation
        # fields = '__all__'
        fields = ['generation', 'id', 'user', 'title']