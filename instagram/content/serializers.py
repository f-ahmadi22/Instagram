from rest_framework import serializers

import user_activity
from .models import Post, Story, Mention
from user.serializers import UserProfilePrivateSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserProfilePrivateSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'location', 'caption', 'user', 'show_likes', 'show_comments',
                  'likes_count', 'comments', 'view_count']

    def get_likes_count(self, obj):
        # Check if show_likes is True
        if obj.show_likes:
            # Return the number of likes for the post
            return obj.get_likes()
        else:
            # If show_likes is False, return None
            return None

    def get_comments(self, obj):
        # Check if show_comments is True
        if obj.show_comments:
            # Return the number of comments for the post
            return obj.get_comments().count()
        else:
            # If show_comments is False, return None
            return None


class StorySerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = ['id', 'location', 'user',
                  'likes_count', 'view_count']

    def get_likes_count(self, obj):
        return obj.get_likes()


class MentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = '__all__'
