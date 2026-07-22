from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user_app.models import User
from .models import Feedback
from .models import Notification


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    filter_horizontal = UserAdmin.filter_horizontal + ('friends',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('friends',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('friends',)}),
    )

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