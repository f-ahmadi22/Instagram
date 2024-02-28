from rest_framework import serializers
from .models import User, UserRelationship


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile_picture', 'bio', 'is_private', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = User.objects.get(username=username, password=password)
        if not user:
            raise serializers.ValidationError('Invalid username or password')

        data['user'] = user
        return data


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserProfilePublicSerializer(serializers.ModelSerializer):
    followings = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    followings_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'profile_picture', 'bio', 'is_private', 'date_joined',
                  'followers_count', 'followings_count', 'followings', 'followers']

    def get_followings_count(self, obj):
        return len(obj.get_followings())

    def get_followers_count(self, obj):
        return len(obj.get_followers())

    def get_followers(self, obj):
        return obj.get_followers()

    def get_followings(self, obj):
        return obj.get_followings()


class UserProfilePrivateSerializer(serializers.ModelSerializer):
    followings_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'profile_picture', 'bio', 'is_private', 'date_joined',
                  'followers_count', 'followings_count']

    def get_followings_count(self, obj):
        return len(obj.get_followings())

    def get_followers_count(self, obj):
        return len(obj.get_followers())
