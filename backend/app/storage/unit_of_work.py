from abc import ABC, abstractmethod

from app.storage.postgres_session import postgres_session_factory
from app.storage.redis_session import redis_session_factory


class IUnitOfWork(ABC):
    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, *args): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...


class UnitOfWork:
    def __init__(self):
        self.postgres_session_factory = postgres_session_factory
        self.redis_session_factory = redis_session_factory

    async def __aenter__(self):
        self.postgres_session = self.postgres_session_factory()
        self.redis_session = self.redis_session_factory()

    async def __aexit__(self, *_):
        await self.postgres_session.aclose()
        await self.redis_session.aclose()

    async def commit(self):
        await self.postgres_session.commit()

    async def rollback(self):
        await self.postgres_session.rollback()

