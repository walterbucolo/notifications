from unittest.mock import Mock
from django.test import TestCase
from notification.helpers.rate_limiter import RateLimiter
from notification.models import Rule, NotificationType


class TestRateLimiter(TestCase):
    def test_it_should_return_false_when_exceeded(self):
        notification_repository = Mock()
        notification_type = NotificationType.objects.create(name="news")
        rule = Rule.objects.create(
            notification_type=notification_type, time_window=300, repetitions=5
        )
        notification_repository.return_value.retrieve.return_value = 5
        rate_limiter = RateLimiter(
            rule=rule, notification_repository=notification_repository
        )

        result = rate_limiter.is_allowed("124798781429")

        self.assertEqual(result, False)

    def test_it_should_return_true_when_key_does_not_exist_in_repository(self):
        notification_repository = Mock()
        notification_type = NotificationType.objects.create(name="news")
        rule = Rule.objects.create(
            notification_type=notification_type, time_window=300, repetitions=5
        )
        notification_repository.return_value.retrieve.return_value = None
        rate_limiter = RateLimiter(
            rule=rule, notification_repository=notification_repository
        )

        result = rate_limiter.is_allowed("124798781429")

        self.assertEqual(result, True)
        notification_repository.return_value.create.assert_called_once()

    def test_it_should_return_true_when_no_exceeded(self):
        notification_repository = Mock()
        notification_type = NotificationType.objects.create(name="news")
        rule = Rule.objects.create(
            notification_type=notification_type, time_window=300, repetitions=5
        )
        notification_repository.return_value.retrieve.return_value = 3
        rate_limiter = RateLimiter(
            rule=rule, notification_repository=notification_repository
        )

        result = rate_limiter.is_allowed("124798781429")

        self.assertEqual(result, True)
        notification_repository.return_value.increment.assert_called_once()
