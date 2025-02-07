from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *  # Or specifically import CustomUser if needed

# Register CustomUser (your custom user model)
User = get_user_model()

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}

class TodoAdmin(admin.ModelAdmin):
    list_editable = ['completed']
    list_display = ['user', 'title' ,'completed', 'date']

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'message', 'is_read', 'date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "name", "email", "comment"]

# Register models
# admin.site.register(ChatMessage, ChatMessageAdmin)
admin.site.register(CustomUser)  # Register your custom user model here
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
