from rest_framework import serializers
from .models import Comment, LikeComment, LikeStory, LikePost


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        fields = '__all__'


class LikeStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeStory
        fields = '__all__'


class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = '__all__'
