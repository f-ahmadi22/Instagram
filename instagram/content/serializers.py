from rest_framework import serializers

import user_activity
from .models import Post, Story, Mention, PostMedia, StoryMedia
from user.serializers import UserProfilePrivateSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserProfilePrivateSerializer(read_only=True)  # Serialize user to get details
    likes_count = serializers.SerializerMethodField()  # Method to get likes count
    comments = serializers.SerializerMethodField()  # Comments of the post
    media = serializers.SerializerMethodField()  # Method to get media

    class Meta:
        model = Post
        fields = ['id', 'location', 'caption', 'user', 'show_likes', 'show_comments',
                  'likes_count', 'comments', 'view_count', 'media']

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

    def get_media(self, obj):
        return PostMediaSerializer(PostMedia.objects.filter(post=obj), many=True).data


class StorySerializer(serializers.ModelSerializer):
    user = UserProfilePrivateSerializer(read_only=True)  # Serialize user to get details
    likes_count = serializers.SerializerMethodField()  # Method to get likes of a story
    media = serializers.SerializerMethodField()  # Method to get media

    class Meta:
        model = Story
        fields = ['id', 'location', 'user',
                  'likes_count', 'view_count', 'media']

    def get_likes_count(self, obj):
        # Return the number of likes for the story
        return obj.get_likes()

    def get_media(self, obj):
        return StoryMediaSerializer(StoryMedia.objects.filter(story=obj), many=True).data


class MentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = '__all__'


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMedia
        fields = '__all__'


class StoryMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryMedia
        fields = '__all__'
