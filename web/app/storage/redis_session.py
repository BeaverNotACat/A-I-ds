import redis.asyncio as redis

from app.settings import settings

def redis_session_factory():
    return redis.from_url(settings.redis_url)

