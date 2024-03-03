from django.contrib import admin
from django.contrib.admin import register
from .models import Comment, LikeComment, LikePost, LikeStory
# Register your models here.


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text', 'created_at', 'is_reply')
    list_display_links = ('id', 'author', 'post', 'text', 'created_at', 'is_reply')
    list_filter = ('author', 'post')
    search_fields = ('author__username', 'post__caption', 'text')
    ordering = ('-created_at',)


@register(LikeComment)
class LikeCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'comment', 'created_at')
    list_display_links = ('id', 'author', 'comment', 'created_at')
    list_filter = ('author', 'comment')
    search_fields = ('author__username', 'comment__text')
    ordering = ('-created_at',)


@register(LikePost)
class LikePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_at')
    list_display_links = ('id', 'author', 'post', 'created_at')
    list_filter = ('author', 'post')
    search_fields = ('author__username', 'post__caption')
    ordering = ('-created_at',)


@register(LikeStory)
class LikeStoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'story', 'created_at')
    list_display_links = ('id', 'author', 'story', 'created_at')
    list_filter = ('author', 'story')
    search_fields = ('author__username',)
    ordering = ('created_at',)

