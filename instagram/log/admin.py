from django.contrib import admin
from django.contrib.admin import register
from .models import ProfileView, PostView, StoryView

# Register your models here.


@register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'timestamp')  # List of fields to display
    list_display_links = ('id', 'user', 'post', 'timestamp')
    list_filter = ('user', 'post')  # Filter fields
    search_fields = ('user__username', 'post__caption')  # Search through these fields
    ordering = ('-timestamp',)  # Order by creation time


@register(StoryView)
class StoryViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'story', 'timestamp')  # List of fields to display
    list_display_links = ('id', 'user', 'story', 'timestamp')
    list_filter = ('user', 'story')  # Filter fields
    search_fields = ('user__username',)  # Search through these fields
    ordering = ('-timestamp',)  # Order by creation time


@register(ProfileView)
class ProfileViewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_profile', 'timestamp')  # List of fields to display
    list_display_links = ('id', 'user', 'user_profile', 'timestamp')
    list_filter = ('user', 'user_profile')  # Filter fields
    search_fields = ('user__username', 'user_profile__username')  # Search through these fields
    ordering = ('-timestamp',)  # Order by creation time


