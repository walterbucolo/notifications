from notification.services.notifications import NotificationService
from notification.gateway.gateway import Gateway


def index(request):
    notification_service = NotificationService(gateway=Gateway)
    notification_service.send("news", "123", "news 1")
    notification_service.send("news", "123", "news 1")
    notification_service.send("news", "123", "news 1")
    notification_service.send("news", "123", "news 1")
