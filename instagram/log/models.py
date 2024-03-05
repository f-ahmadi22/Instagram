from django.db import models
from user.models import MyUser
from content.models import Post, Story

# Create your models here.


class ProfileView(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='profile_viewer', verbose_name='user')
    user_profile = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='profile_view',
                                     verbose_name='user profile')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='timestamp')

    def __str__(self):
        return f'{self.user.username} viewed {self.user_profile.username}'


class PostView(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='post_viewer', verbose_name='user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_view', verbose_name='post')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='timestamp')

    def __str__(self):
        return f'{self.user.username} viewed {self.post.id}'
