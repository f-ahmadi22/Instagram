from django.contrib import admin
from django.contrib.admin import register
from .models import MyUser, UserRelationship

# Register your models here.


@register(MyUser)
class UserAdmin(admin.ModelAdmin):
    model = MyUser
    list_display = ('id', 'username', 'email', 'profile_picture', 'bio', 'date_joined', 'is_active', 'is_staff',
                    'is_superuser', 'is_private')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'profile_picture', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_private')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('pk',)


@register(UserRelationship)
class UserRelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'following', 'created_at')
    list_display_links = ('id', 'follower', 'following')
    search_fields = ('follower', 'following')
    ordering = ('id',)

