from django.contrib import admin
from .models import Whiteboard


# Register your models here.
@admin.register(Whiteboard)
class WhiteboardAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "created_at", "updated_at"]
    search_fields = ["name", "description"]
    list_filter = ["created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
