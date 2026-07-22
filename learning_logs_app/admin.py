from django.contrib import admin
from .models import Topic
from .models import Entry
from .models import ErrorLog

admin.site.register(Topic)
admin.site.register(Entry)

@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'path', 'exception_type', 'is_resolved')
    list_filter = ('is_resolved', 'timestamp')
    search_fields = ('path', 'exception_type', 'exception_message')
    readonly_fields = ('timestamp', 'path', 'method', 'exception_type', 'exception_message', 'traceback')
    ordering = ('-timestamp',)