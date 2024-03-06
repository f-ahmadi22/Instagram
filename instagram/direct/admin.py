from django.contrib import admin
from django.contrib.admin import register
from .models import DialogsModel, MessageModel
# Register your models here.


@register(DialogsModel)
class DialogsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user1', 'user2')  # List of fields to display
    list_display_links = ('id', 'user1', 'user2')
    search_fields = ('user1', 'user2')  # Search through these fields
    list_filter = ('user1', 'user2')  # Filter fields


@register(MessageModel)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'recipient', 'text', 'read')  # List of fields to display
    list_display_links = ('id', 'sender', 'recipient', 'text')
    list_editable = ('read',)  # Editable fields from panel
    search_fields = ('sender', 'recipient', 'text')  # Search through these fields
    list_filter = ('sender', 'recipient', 'read')  # Filter fields
