from django.db import models
from user.models import MyUser


class Media(models.Model):
    file = models.FileField(upload_to='media/content/')


class Tag(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Mention(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    story = models.ForeignKey('Story', related_name='mentions', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='post', verbose_name='author')
    location = models.CharField(max_length=255, verbose_name='location', blank=True, null=True)
    caption = models.CharField(max_length=255, verbose_name='caption', blank=True, null=True)
    show_comments = models.BooleanField(verbose_name='show comments', default=True)
    show_likes = models.BooleanField(verbose_name='show likes', default=True)
    show_views = models.BooleanField(verbose_name='show views', default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_comments(self):
        return self

    def get_likes(self):
        return self

    def get_views(self):
        return self


class PostMedia(models.Model):
    post = models.ForeignKey(Post, related_name='media', on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)  # Order of media in a post


class Story(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='story', verbose_name='author')
    location = models.CharField(max_length=255, verbose_name='location', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='is active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation date')

    def __str__(self):
        return self.user.username

    def get_likes(self):
        return self

    def get_views(self):
        return self


class StoryMedia(models.Model):
    story = models.ForeignKey(Story, related_name='media', on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)  # Order of media in a story
