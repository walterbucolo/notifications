from typing import Optional
from notification.models import Rule
from notification.repositories.interface import (
    INotificationRepository,
)
from notification.repositories.redis import RedisNotificationRepository


class RateLimiter:
    def __init__(
        self,
        rule: type[Rule],
        notification_repository: Optional[INotificationRepository] = None,
    ):
        if not notification_repository:
            notification_repository = RedisNotificationRepository
        self.notification_repository = notification_repository()
        self.rule = rule

    def is_allowed(self, user_id: str) -> bool:

        key = f"{user_id}:{self.rule.notification_type}"
        current_count = self.notification_repository.retrieve(key)
        if not current_count:
            self.notification_repository.create(key, 1, ex=self.rule.time_window)
            return True
        if int(current_count) < self.rule.repetitions:
            self.notification_repository.increment(key)
            return True

        return False
