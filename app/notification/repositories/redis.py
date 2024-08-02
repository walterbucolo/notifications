from typing import Optional
import redis
from notification.repositories.interface import (
    INotificationRepository,
)
from django.conf import settings


class RedisClient:
    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            print("Creating new Redis client")
            print("<<<<settings>>>>")
            print(settings.REDIS_HOST)
            print(settings.REDIS_PORT)
            print(settings.REDIS_DB)
            print(settings.REDIS_MAX_CONNECTIONS)
            pool = redis.ConnectionPool(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB,
            )
            cls._client = redis.Redis(connection_pool=pool)
        return cls._client


class RedisNotificationRepository(INotificationRepository):
    def __init__(self, redis_client: Optional[redis.Redis] = None):
        if redis_client is None:
            redis_client = RedisClient.get_client()

        self.redis_client = redis_client

    def retrieve(self, key: str):
        return self.redis_client.get(key)

    def create(self, key: str, value: str, ex: int):
        return self.redis_client.set(key, value, ex=ex)

    def increment(self, key: str):
        return self.redis_client.incr(key)
