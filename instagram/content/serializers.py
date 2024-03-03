from rest_framework import serializers
from .models import Post, Story, Mention


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class MentionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mention
        fields = '__all__'
