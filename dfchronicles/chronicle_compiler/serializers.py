from rest_framework import serializers
from .models import World

class WorldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ['id', 'name', 'name2', 'owner']

class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ['id', 'name', 'name2', 'owner', 'world_artifacts']