from rest_framework import serializers
from .models import MyUser, UserRelationship


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password', 'profile_picture', 'bio', 'is_private', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):  # Serialize data to create a user
        user = MyUser.objects.create(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # Serialize username field
    password = serializers.CharField()  # Serialize password field

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = MyUser.objects.get(username=username, password=password)  # Get user by username and password
        if not user:
            raise serializers.ValidationError('Invalid username or password')  # Return error if got invalid credentials

        data['user'] = user
        return data  # Return user data if login was validated


class UserProfileSerializer(serializers.ModelSerializer):  # User profile serializer
    class Meta:
        model = MyUser
        fields = '__all__'


class UserProfilePublicSerializer(serializers.ModelSerializer):  # User profile public serializer
    followings = serializers.SerializerMethodField()  # Serializer method to get followings of a user
    followers = serializers.SerializerMethodField()  # Serializer method to get followers of a user
    followings_count = serializers.SerializerMethodField()  # Serializer method to get following count of a user
    followers_count = serializers.SerializerMethodField()  # Serializer method to get follower count of a user

    class Meta:
        model = MyUser
        fields = ['username', 'profile_picture', 'bio', 'is_private', 'date_joined',
                  'followers_count', 'followings_count', 'followings', 'followers', 'view_count']

    def get_followings_count(self, obj):
        return len(obj.get_followings())  # Return number of following of user

    def get_followers_count(self, obj):
        return len(obj.get_followers())  # Return number of followers of user

    def get_followers(self, obj):
        followers = obj.get_followers()
        # Return details of followers of user
        return [UserProfilePrivateSerializer(MyUser.objects.get(id=follower)).data for follower in followers]

    def get_followings(self, obj):
        followings = obj.get_followings()
        # Return details of followings of user
        return [UserProfilePrivateSerializer(MyUser.objects.get(id=following)).data for following in followings]


class UserProfilePrivateSerializer(serializers.ModelSerializer):
    followings_count = serializers.SerializerMethodField()  # Serializer method to get following count of a user
    followers_count = serializers.SerializerMethodField()  # Serializer method to get follower count of a user

    class Meta:
        model = MyUser
        fields = ['username', 'profile_picture', 'bio', 'is_private', 'date_joined',
                  'followers_count', 'followings_count', 'view_count']

    def get_followings_count(self, obj):
        return len(obj.get_followings())  # Return number of following of user

    def get_followers_count(self, obj):
        return len(obj.get_followers())  # Return number of followers of user
