from django.db import models
from user.models import MyUser
from content.models import Post, Story


# Create your models here.


class Comment(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='comments', verbose_name='author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='post')
    text = models.TextField(verbose_name='text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    is_reply = models.BooleanField(default=False, verbose_name='is reply')

    def __str__(self):
        return self.text

#    def replies(self):
#        return self

    def likes(self):
        return LikeComment.objects.filter(comment=self).count()


class LikePost(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='like_post', verbose_name='author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post', verbose_name='post')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')

    def __str__(self):
        return f'{self.author.username} liked post {self.post.id}'


class LikeComment(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='like_comment', verbose_name='author')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='like_comment', verbose_name='comment')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')

    def __str__(self):
        return f'{self.author.username} liked comment {self.comment.id}'


class LikeStory(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='like_story', verbose_name='author')
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='like_story', verbose_name='story')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')

    def __str__(self):
        return f'{self.author.username} liked story {self.story.id}'
