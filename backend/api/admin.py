from django.contrib import admin
from.models import *
from api.models import Todo, ChatMessage
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_editable = ['completed']
    list_display = ['user', 'title' ,'completed', 'date']

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'message', 'is_read', 'date']

admin.site.register(ChatMessage, ChatMessageAdmin)
admin.site.register(CustomUser)

