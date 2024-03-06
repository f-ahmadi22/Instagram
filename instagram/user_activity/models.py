from django.db import models
from user.models import MyUser
from content import models as m


# Create your models here.


class Comment(models.Model):
    # Comment author
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='comments', verbose_name='author')
    # Post on which the user comments
    post = models.ForeignKey(m.Post, on_delete=models.CASCADE, related_name='comments', verbose_name='post')
    text = models.TextField(verbose_name='text')  # Comment's text
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')  # Creation time
    is_reply = models.BooleanField(default=False, verbose_name='is reply')  # Is reply or not

    def __str__(self):
        return self.text

#    def replies(self):
#        return self

    def likes(self):  # Get likes count of a given comment
        return LikeComment.objects.filter(comment=self).count()


class LikePost(models.Model):
    # User who likes
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='like_post', verbose_name='author')
    # Post which is being liked
    post = models.ForeignKey(m.Post, on_delete=models.CASCADE, related_name='like_post', verbose_name='post')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')  # The time of like

    def __str__(self):
        return f'{self.author.username} liked post {self.post.id}'


class LikeComment(models.Model):
    # User who likes
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='like_comment', verbose_name='author')
    # Comment which is being liked
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='like_comment', verbose_name='comment')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')  # The time of like

    def __str__(self):
        return f'{self.author.username} liked comment {self.comment.id}'


class LikeStory(models.Model):
    # User who likes
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='like_story', verbose_name='author')
    # Story which is being liked
    story = models.ForeignKey(m.Story, on_delete=models.CASCADE, related_name='like_story', verbose_name='story')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')  # The time of like

    def __str__(self):
        return f'{self.author.username} liked story {self.story.id}'
