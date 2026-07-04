from django.contrib import admin
from .models import Topic
from .models import Entry
from .models import ErrorLog
from .models import Feedback

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