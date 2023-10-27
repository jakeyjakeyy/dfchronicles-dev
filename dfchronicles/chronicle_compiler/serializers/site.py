from rest_framework import serializers
from ..models import Sites, Structures

class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sites
        fields = ['name', 'type']
        
class StructuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structures
        fields = ['name', 'type']