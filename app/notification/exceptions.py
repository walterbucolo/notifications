class NotificationServiceError(Exception):
    message = "Notification service error"
    status_code = 500


class NotificationTypeNotFound(NotificationServiceError):
    message = "Invalid notification type"
    status_code = 404


class RuleNotFound(NotificationServiceError):
    message = "No rule found for the notification type"
    status_code = 404


class RateLimitExceeded(NotificationServiceError):
    message = "Rate limit exceeded"
    status_code = 403
