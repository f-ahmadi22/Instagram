from django.contrib import admin
from django.contrib.admin import register
from .models import Post, PostMedia, Story, StoryMedia, Mention, Tag
# Register your models here.


class PostMediaInline(admin.StackedInline):  # Post Inline class
    model = PostMedia
    extra = 1  # Just one extra object


class StoryMediaInline(admin.StackedInline):  # Story Inline class
    model = StoryMedia
    extra = 1  # Just one extra object


@register(Post)
class PostAdmin(admin.ModelAdmin):
    Inlines = [PostMediaInline]
    list_display = ('id', 'user', 'caption', 'location', 'show_comments', 'show_likes', 'created_at')
    list_display_links = ('id', 'user', 'caption', 'location', 'created_at')
    list_editable = ('show_comments', 'show_likes')
    search_fields = ('user__username', 'caption')
    ordering = ('id',)


@register(PostMedia)
class PostMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'media', 'order')
    list_display_links = ('id', 'post', 'media', 'order')
    ordering = ('id',)


@register(Story)
class StoryAdmin(admin.ModelAdmin):
    Inlines = [StoryMediaInline]
    list_display = ('id', 'user', 'location', 'created_at', 'is_active')
    list_display_links = ('id', 'user', 'location', 'created_at')
    list_editable = ('is_active',)
    ordering = ('id',)


@register(StoryMedia)
class StoryMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'story', 'media', 'order')
    list_display_links = ('id', 'story', 'media', 'order')
    ordering = ('id',)


@register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'story')
    list_display_links = ('id', 'user', 'story')
    ordering = ('id',)


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')
    list_display_links = ('id', 'user', 'post')
    ordering = ('id',)


