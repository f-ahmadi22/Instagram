from rest_framework import serializers
from .models import User, UserRelationship


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_picture', 'bio', 'is_private', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class UserProfilePublicSerializer(serializers.ModelSerializer):
    followings = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    followings_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'profile_picture', 'bio', 'is_private', 'created_at',
                  'followers_count', 'followings_count', 'followings', 'followers']

    def get_followings_count(self, obj):
        return obj.get_followings_count()

    def get_followers_count(self, obj):
        return obj.get_followers_count()

    def get_followers(self, obj):
        return obj.get_followers()

    def get_followings(self, obj):
        return obj.get_followings()


class UserProfilePrivateSerializer(serializers.ModelSerializer):
    followings_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'profile_picture', 'bio', 'is_private', 'created_at',
                  'followers_count', 'followings_count']

    def get_followings_count(self, obj):
        return obj.get_followings_count()

    def get_followers_count(self, obj):
        return obj.get_followers_count()
