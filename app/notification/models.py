from django.db import models


class NotificationType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Rule(models.Model):
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    time_window = models.IntegerField(help_text="Time window in seconds")
    repetitions = models.IntegerField(help_text="Number of repetitions allowed")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.notification_type} - {self.time_window} - {self.repetitions}"


class NotificationLog(models.Model):
    user_id = models.CharField(max_length=255)
    type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id}"
