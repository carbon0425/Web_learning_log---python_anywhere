from django.contrib import admin
from .models import Topic
from .models import Entry
from .models import ErrorLog
from .models import Feedback
from .models import Notification

admin.site.register(Topic)
admin.site.register(Entry)

@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'path', 'exception_type', 'is_resolved')
    list_filter = ('is_resolved', 'timestamp')
    search_fields = ('path', 'exception_type', 'exception_message')
    readonly_fields = ('timestamp', 'path', 'method', 'exception_type', 'exception_message', 'traceback')
    ordering = ('-timestamp',)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at')
    search_fields = ('username', 'email', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message_preview', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('username', 'message_preview', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    def message_preview(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message preview'