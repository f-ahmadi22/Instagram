from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='email address')
    username = models.CharField(max_length=100, unique=True, verbose_name='username')
    profile_picture = models.ImageField(upload_to='profile_pictures/', verbose_name='profile picture',
                                        null=True, blank=True)
    bio = models.TextField(verbose_name='biography', blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='date')
    is_active = models.BooleanField(default=True, verbose_name='active')
    is_staff = models.BooleanField(default=False, verbose_name='staff')
    is_superuser = models.BooleanField(default=False, verbose_name='superuser')
    is_private = models.BooleanField(verbose_name='private', default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def get_followings(self):
        # Get followings of given user
        followings = UserRelationship.objects.filter(follower=self).values_list('following', flat=True)
        return followings

    def get_followers(self):
        # Get followers of given user
        followers = UserRelationship.objects.filter(following=self).values_list('follower', flat=True)
        return followers


class UserRelationship(models.Model):
    # user who follows
    follower = models.ForeignKey(MyUser, related_name='following', verbose_name='follower', on_delete=models.CASCADE)
    # user who's being followed
    following = models.ForeignKey(MyUser, related_name='followers', verbose_name='following', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'
