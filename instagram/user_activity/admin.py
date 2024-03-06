from django.contrib import admin
from django.contrib.admin import register
from .models import Comment, LikeComment, LikePost, LikeStory
# Register your models here.


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text', 'created_at', 'is_reply')  # List of fields to display
    list_display_links = ('id', 'author', 'post', 'text', 'created_at', 'is_reply')
    list_filter = ('author', 'post')  # Filter fields
    search_fields = ('author__username', 'post__caption', 'text')  # Search through these fields
    ordering = ('-created_at',)  # Order by creation time


@register(LikeComment)
class LikeCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'comment', 'created_at')  # List of fields to display
    list_display_links = ('id', 'author', 'comment', 'created_at')
    list_filter = ('author', 'comment')  # Filter fields
    search_fields = ('author__username', 'comment__text')  # Search through these fields
    ordering = ('-created_at',)  # Order by creation time


@register(LikePost)
class LikePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_at')  # List of fields to display
    list_display_links = ('id', 'author', 'post', 'created_at')
    list_filter = ('author', 'post')  # Filter fields
    search_fields = ('author__username', 'post__caption')  # Search through these fields
    ordering = ('-created_at',)  # Order by creation time


@register(LikeStory)
class LikeStoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'story', 'created_at')  # List of fields to display
    list_display_links = ('id', 'author', 'story', 'created_at')
    list_filter = ('author', 'story')  # Filter fields
    search_fields = ('author__username',)  # Search through these fields
    ordering = ('created_at',)  # Order by creation time

