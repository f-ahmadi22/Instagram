from django.contrib import admin
from django.contrib.admin import register
from .models import Post, PostMedia, Story, StoryMedia, Mention, Tag
# Register your models here.


class PostMediaInline(admin.StackedInline):  # Post Inline class
    model = PostMedia  # To add media to a post
    extra = 1  # Just one extra object


class StoryMediaInline(admin.StackedInline):  # Story Inline class
    model = StoryMedia # To add media to a story
    extra = 1  # Just one extra object


class MentionInline(admin.StackedInline):  # Mention Inline class
    model = Mention
    extra = 1  # Just one extra object


class TagInline(admin.StackedInline):  # Tag Inline class
    model = Tag
    extra = 1  # Just one extra object


@register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostMediaInline, TagInline]  # Inline classes
    # List of fields to display
    list_display = ('id', 'user', 'caption', 'location', 'show_comments', 'show_likes', 'created_at')
    list_display_links = ('id', 'user', 'caption', 'location', 'created_at')
    list_editable = ('show_comments', 'show_likes')  # Editable fields from panel
    search_fields = ('user__username', 'caption')  # Search through these fields
    ordering = ('id',)  # Order by id


@register(PostMedia)
class PostMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'media', 'order')  # List of fields to display
    list_display_links = ('id', 'post', 'media', 'order')
    ordering = ('id',)  # Order by id


@register(Story)
class StoryAdmin(admin.ModelAdmin):
    inlines = [StoryMediaInline, MentionInline]  # Inline classes
    list_display = ('id', 'user', 'location', 'created_at', 'is_active')  # List of fields to display
    list_display_links = ('id', 'user', 'location', 'created_at')
    list_editable = ('is_active',)  # Editable fields from panel
    ordering = ('id',)  # Order by id


@register(StoryMedia)
class StoryMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'story', 'media', 'order')  # List of fields to display
    list_display_links = ('id', 'story', 'media', 'order')
    ordering = ('id',)  # Order by id


@register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'story')  # List of fields to display
    list_display_links = ('id', 'user', 'story')
    ordering = ('id',)  # Order by id


@register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')  # List of fields to display
    list_display_links = ('id', 'user', 'post')
    ordering = ('id',)  # Order by id


