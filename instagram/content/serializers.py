from rest_framework import serializers
from .models import Post, Story, Mention
from user.serializers import UserProfilePrivateSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserProfilePrivateSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'location', 'caption', 'user', 'show_likes', 'show_comments', 'view_count']


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class MentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = '__all__'
