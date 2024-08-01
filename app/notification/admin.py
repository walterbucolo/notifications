from django.contrib import admin
from notification.models import NotificationType, Rule


@admin.register(NotificationType, Rule)
class NotificationTypeAdmin(admin.ModelAdmin):
    pass
