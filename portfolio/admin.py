from django.contrib import admin
from .models import Message, Project


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'short_text', 'created_at')
    search_fields = ('name', 'email', 'text')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('name', 'email', 'text', 'created_at')
    list_per_page = 10

    def short_text(self, obj):
        return (obj.text[:50] + '...') if len(obj.text) > 50 else obj.text
    short_text.short_description = "Сообщение"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short', 'created_at', 'is_featured')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'is_featured')
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_featured',)
    list_per_page = 10

    def description_short(self, obj):
        return (obj.description[:60] + '...') if len(obj.description) > 60 else obj.description
    description_short.short_description = "Описание"
