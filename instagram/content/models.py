from django.db import models

import user_activity
from user.models import MyUser


class Post(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts', verbose_name='author')  # Author
    location = models.CharField(max_length=255, verbose_name='location', blank=True, null=True)  # Location
    caption = models.CharField(max_length=255, verbose_name='caption', blank=True, null=True)  # Post caption
    show_comments = models.BooleanField(verbose_name='show comments', default=True)  # Show comments count if true
    show_likes = models.BooleanField(verbose_name='show likes', default=True)  # Show likes count if true
    view_count = models.IntegerField(verbose_name='views', default=0)  # views count
    created_at = models.DateTimeField(auto_now_add=True)  # creation time

    def __str__(self):
        return f'{self.id}'

    def get_comments(self):  # Get comments of a given post
        return user_activity.models.Comment.objects.filter(post=self).order_by('-created_at')

    def get_likes(self):  # Get number of likes of a given post
        return user_activity.models.LikePost.objects.filter(post=self).count()


class PostMedia(models.Model):
    post = models.ForeignKey(Post, related_name='post_media', on_delete=models.CASCADE, verbose_name='post')  # Post
    media = models.FileField(upload_to='media/content/post/', verbose_name='post media file')  # File of media
    order = models.PositiveIntegerField(default=0)  # Order of media in a post


class Story(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='stories', verbose_name='author')  # Author
    location = models.CharField(max_length=255, verbose_name='location', blank=True, null=True)  # Location
    view_count = models.IntegerField(verbose_name='views', default=0)  # Views count number
    is_active = models.BooleanField(default=True, verbose_name='is active')  # Is active or not
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation date')  # Creation time

    def __str__(self):
        return f'{self.id}'

    def get_likes(self):  # Get likes count of the given story
        return user_activity.models.LikeStory.objects.filter(story=self).count()


class StoryMedia(models.Model):
    # story referred
    story = models.ForeignKey(Story, related_name='story_media', on_delete=models.CASCADE, verbose_name='story')
    media = models.FileField(upload_to='media/content/story/', verbose_name='story media file')  # Media file related
    order = models.PositiveIntegerField(default=0)  # Order of media in a story


class Tag(models.Model):  # Post author tag user in his post
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='tags', verbose_name='user')  # User tagged
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tags', verbose_name='post')  # Post

    def __str__(self):
        return self.user.username


class Mention(models.Model):  # Story author mention user in his story
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='mentions', verbose_name='user')  # User
    story = models.ForeignKey(Story, related_name='mentions', on_delete=models.CASCADE)  # Story

    def __str__(self):
        return self.user.username
