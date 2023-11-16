from rest_framework import serializers
from .models import Generation, Comment

class GenerationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Generation
        # fields = '__all__'
        fields = ['generation', 'id', 'user', 'title']
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ['user', 'generation', 'comment', 'time', 'id']