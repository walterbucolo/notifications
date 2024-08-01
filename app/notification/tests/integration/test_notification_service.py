from django.test import TestCase, override_settings
from redis import Redis
from notification.exceptions import RateLimitExceeded
from notification.models import NotificationLog, NotificationType, Rule
from notification.gateway.gateway import Gateway
from notification.services.notifications import NotificationService
from freezegun import freeze_time
from django.utils import timezone


class TestNotificationService(TestCase):
    def setUp(self):
        gateway = Gateway()
        self.notification_service = NotificationService(gateway=gateway)

    @override_settings(REDIS_HOST="redis", REDIS_PORT=6379)
    def test_send_notification_with_repetitions(self):
        notification_type = NotificationType.objects.create(name="news")
        Rule.objects.create(
            notification_type=notification_type, time_window=300, repetitions=2
        )
        now = timezone.now()
        with freeze_time(now):
            self.notification_service.send("news", "243978", "first message")
            self.notification_service.send("news", "243978", "second message")

        with self.assertRaises(RateLimitExceeded):
            self.notification_service.send("news", "243978", "third message")

        self.assertTrue(
            NotificationLog.objects.filter(
                user_id="243978",
                message="first message",
                created_at=now,
            ).exists()
        )

    def tearDown(self) -> None:
        Redis(host="redis", port=6379).flushall()
