from rest_framework import serializers
from .models import Generation, Comment, Rating, User

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Rating
        fields = ['user', 'rating', 'generation', 'time', 'id']

class GenerationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    ratings = RatingSerializer(many=True, read_only=True)
    class Meta:
        model = Generation
        fields = ['generation', 'id', 'user', 'title', 'ratings', 'favorites']
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Comment
        fields = ['user', 'generation', 'comment', 'time', 'id']
        
class UserSerializer(serializers.ModelSerializer):
    generations = GenerationSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'generations', 'user_favorites', 'user_comments']