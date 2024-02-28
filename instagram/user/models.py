from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100, verbose_name='username', null=False, blank=False)  # Username field
    email = models.EmailField(unique=True, verbose_name='email', null=False, blank=False)  # Email field
    password = models.CharField(max_length=100, verbose_name='password')  # Password field
    profile_picture = models.ImageField(upload_to='profile_pictures/', verbose_name='profile picture',
                                        null=True, blank=True)  # Profile picture field (optional)
    bio = models.TextField(verbose_name='biography', blank=True)  # Biography text field (optional)
    date_joined = models.DateTimeField(auto_now_add=True)  # Time of user signup
    is_private = models.BooleanField(verbose_name='private', default=False)  # Private or public

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
