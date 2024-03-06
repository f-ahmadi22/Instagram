from rest_framework import serializers
from .models import Comment, LikeComment, LikeStory, LikePost
from user.serializers import UserProfilePrivateSerializer
from content.serializers import PostSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = UserProfilePrivateSerializer(read_only=True)  # Serialize user to show details
    post = PostSerializer()  # Serialize post to show details
    likes = serializers.SerializerMethodField()  # Serializer method to get likes count

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'likes', 'created_at']

    def get_likes(self, obj):
        # Return likes count of a comment
        return obj.likes()


class LikeCommentSerializer(serializers.ModelSerializer):
    author = UserProfilePrivateSerializer(read_only=True)  # Serialize user to show details
    comment = CommentSerializer()  # Serialize comment to show details

    class Meta:
        model = LikeComment
        fields = ['id', 'author', 'comment', 'created_at']


class LikeStorySerializer(serializers.ModelSerializer):
    author = UserProfilePrivateSerializer(read_only=True)  # Serialize user to show details

    class Meta:
        model = LikeStory
        fields = ['id', 'author', 'story', 'created_at']


class LikePostSerializer(serializers.ModelSerializer):
    author = UserProfilePrivateSerializer(read_only=True)  # Serialize user to show details
    post = PostSerializer()  # Serialize post to show details

    class Meta:
        model = LikePost
        fields = ['id', 'author', 'post', 'created_at']
