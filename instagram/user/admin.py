from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, UserRelationship, FollowRequest


class MyUserAdmin(UserAdmin):
    model = MyUser
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'profile_picture', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_private')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    list_display = ('id', 'username', 'email', 'profile_picture', 'bio', 'date_joined', 'is_active', 'is_staff',
                    'is_superuser', 'is_private', 'view_count')  # List of fields to display
    search_fields = ('username', 'email')  # Search through these fields
    ordering = ('id',)  # Order by id


admin.site.register(MyUser, MyUserAdmin)


@admin.register(UserRelationship)
class UserRelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'follower', 'following', 'created_at')  # List of fields to display
    list_display_links = ('id', 'follower', 'following')
    search_fields = ('follower__username', 'following__username')  # Search through these fields
    ordering = ('id',)  # Order by id


@admin.register(FollowRequest)
class FollowRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'created_at')  # List of fields to display
    list_display_links = ('id', 'sender', 'receiver', 'created_at')
    search_fields = ('sender__username', 'receiver__username')  # Search through these fields
    ordering = ('-created_at',)  # Order by creation time

