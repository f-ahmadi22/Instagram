from rest_framework import serializers
from .models import Comment, LikeComment, LikeStory, LikePost
from user.serializers import UserProfilePrivateSerializer
from content.serializers import PostSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = UserProfilePrivateSerializer(read_only=True)
    post = PostSerializer()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'likes', 'created_at']

    def get_likes(self, obj):
        return obj.likes()


class LikeCommentSerializer(serializers.ModelSerializer):
    author = UserProfilePrivateSerializer(read_only=True)
    comment = CommentSerializer()

    class Meta:
        model = LikeComment
        fields = ['id', 'author', 'comment', 'created_at']


class LikeStorySerializer(serializers.ModelSerializer):
    author = UserProfilePrivateSerializer(read_only=True)

    class Meta:
        model = LikeStory
        fields = ['id', 'author', 'story', 'created_at']


class LikePostSerializer(serializers.ModelSerializer):
    author = UserProfilePrivateSerializer(read_only=True)
    post = PostSerializer()

    class Meta:
        model = LikePost
        fields = ['id', 'author', 'post', 'created_at']
