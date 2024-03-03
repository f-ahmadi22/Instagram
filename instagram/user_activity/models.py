from django.db import models
from user.models import MyUser
from content.models import Post


# Create your models here.


class Comment(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='comments', verbose_name='author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='post')
    text = models.TextField(verbose_name='text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    is_reply = models.BooleanField(default=False, verbose_name='is reply')

    def __str__(self):
        return self.text

    def replies(self):
        return self

    def likes(self):
        return self
