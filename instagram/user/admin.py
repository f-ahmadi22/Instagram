from django.contrib import admin
from django.contrib.admin import register
from .models import User, UserRelationship

# Register your models here.


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_private', 'bio')
    list_display_links = ('id', 'username', 'email', 'bio', 'is_private')
    list_filter = ('is_private',)
    search_fields = ('username', 'bio')
    ordering = ('id',)


@register(UserRelationship)
class UserRelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'following', 'created_at')
    list_display_links = ('id', 'follower', 'following')
    search_fields = ('follower', 'following')
    ordering = ('id',)

