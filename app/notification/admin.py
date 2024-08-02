from django.contrib import admin
from notification.models import NotificationType, Rule, NotificationLog


@admin.register(NotificationType, Rule, NotificationLog)
class NotificationTypeAdmin(admin.ModelAdmin):
    pass
