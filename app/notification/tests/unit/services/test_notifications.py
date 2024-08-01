from unittest.mock import Mock, patch
from django.test import TestCase
from notification.exceptions import (
    NotificationTypeNotFound,
    RateLimitExceeded,
    RuleNotFound,
)
from notification.models import NotificationLog, NotificationType, Rule
from notification.services.notifications import NotificationService


class TestNotificationService(TestCase):
    def test_it_should_raise_when_notification_is_not_found(self):
        gateway = Mock()

        with self.assertRaises(NotificationTypeNotFound) as exc:
            NotificationService(gateway=gateway).send("news", "124798781429", "message")

        self.assertEqual(exc.exception.message, "Invalid notification type")
        self.assertEqual(exc.exception.status_code, 404)

    def test_it_should_raise_when_rule_is_not_found(self):
        gateway = Mock()
        NotificationType.objects.create(name="news")

        with self.assertRaises(RuleNotFound) as exc:
            NotificationService(gateway=gateway).send("news", "124798781429", "message")

        self.assertEqual(
            exc.exception.message, "No rule found for the notification type"
        )
        self.assertEqual(exc.exception.status_code, 404)

    @patch("notification.helpers.rate_limiter.RateLimiter.is_allowed")
    def test_it_should_raise_when_rate_limit_exceeded(self, mock_rate_limiter):
        gateway = Mock()
        notification_type = NotificationType.objects.create(name="news")
        Rule.objects.create(
            notification_type=notification_type, time_window=3200, repetitions=10
        )
        mock_rate_limiter.return_value = False

        with self.assertRaises(RateLimitExceeded) as exc:
            NotificationService(gateway=gateway).send("news", "124798781429", "message")

        self.assertEqual(exc.exception.message, "Rate limit exceeded")
        self.assertEqual(exc.exception.status_code, 403)

    @patch("notification.helpers.rate_limiter.RateLimiter.is_allowed")
    def test_it_should_send_notification(self, mock_rate_limiter):
        gateway = Mock()
        notification_type = NotificationType.objects.create(name="news")
        Rule.objects.create(
            notification_type=notification_type, time_window=3200, repetitions=10
        )
        mock_rate_limiter.return_value = True

        NotificationService(gateway=gateway).send("news", "124798781429", "message")

        gateway.send.assert_called_once_with("124798781429", "message")
        self.assertTrue(
            NotificationLog.objects.filter(
                user_id="124798781429", message="message", type=notification_type
            ).exists()
        )
