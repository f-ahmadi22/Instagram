from django.db import models

import user_activity
from user.models import MyUser


class Post(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts', verbose_name='author')
    location = models.CharField(max_length=255, verbose_name='location', blank=True, null=True)
    caption = models.CharField(max_length=255, verbose_name='caption', blank=True, null=True)
    show_comments = models.BooleanField(verbose_name='show comments', default=True)
    show_likes = models.BooleanField(verbose_name='show likes', default=True)
    view_count = models.IntegerField(verbose_name='views', default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'

    def get_comments(self):
        return user_activity.models.Comment.objects.filter(post=self).order_by('-created_at')

    def get_likes(self):
        return user_activity.models.LikePost.objects.filter(post=self).count()


class PostMedia(models.Model):
    post = models.ForeignKey(Post, related_name='post_media', on_delete=models.CASCADE, verbose_name='post')
    media = models.FileField(upload_to='media/content/post/', verbose_name='post media file')
    order = models.PositiveIntegerField(default=0)  # Order of media in a post


class Story(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='stories', verbose_name='author')
    location = models.CharField(max_length=255, verbose_name='location', blank=True, null=True)
    view_count = models.IntegerField(verbose_name='views', default=0)
    is_active = models.BooleanField(default=True, verbose_name='is active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation date')

    def __str__(self):
        return f'{self.id}'

    def get_likes(self):
        return user_activity.models.LikeStory.objects.filter(story=self).count()


class StoryMedia(models.Model):
    story = models.ForeignKey(Story, related_name='story_media', on_delete=models.CASCADE, verbose_name='story')
    media = models.FileField(upload_to='media/content/story/', verbose_name='story media file')
    order = models.PositiveIntegerField(default=0)  # Order of media in a story


class Tag(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='tags', verbose_name='user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tags', verbose_name='post')

    def __str__(self):
        return self.user.username


class Mention(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='mentions', verbose_name='user')
    story = models.ForeignKey(Story, related_name='mentions', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
