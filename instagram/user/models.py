from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)  # Email field
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, verbose_name='username', null=False, blank=False)  # Username field
    password = models.CharField(max_length=100, verbose_name='password')  # Password field
    profile_picture = models.ImageField(upload_to='profile_pictures/', verbose_name='profile picture',
                                        null=True, blank=True)  # Profile picture field (optional)
    bio = models.TextField(verbose_name='biography', blank=True)  # Biography text field (optional)
    is_private = models.BooleanField(verbose_name='private', default=False)  # Private or public

    objects = CustomUserManager()

    def __str__(self):
        # Return username
        return self.username

    def get_followings(self):
        # Get followings of given user
        return UserRelationship.objects.filter(follower=self)

    def get_followers(self):
        # Get followers of given user
        return UserRelationship.objects.filter(following=self)


class UserRelationship(models.Model):
    # user who follows
    follower = models.ForeignKey(User, related_name='following', verbose_name='follower', on_delete=models.CASCADE)
    # user who's being followed
    following = models.ForeignKey(User, related_name='followers', verbose_name='following', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'
