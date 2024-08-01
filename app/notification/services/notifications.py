from notification.exceptions import (
    NotificationTypeNotFound,
    RateLimitExceeded,
    RuleNotFound,
)
from notification.models import NotificationLog, NotificationType, Rule
from notification.helpers.rate_limiter import RateLimiter


class NotificationService:
    def __init__(self, gateway):
        self.gateway = gateway

    def send(self, type: str, user_id: str, message: str):
        try:
            notification_type = NotificationType.objects.get(name=type)
        except NotificationType.DoesNotExist:
            raise NotificationTypeNotFound()

        try:
            rule = Rule.objects.get(notification_type=notification_type)
        except Rule.DoesNotExist:
            raise RuleNotFound()

        if RateLimiter(rule=rule).is_allowed(user_id):
            self.gateway.send(user_id, message)
            NotificationLog.objects.create(
                user_id=user_id, type=notification_type, message=message
            )
        else:
            raise RateLimitExceeded()
