import uuid

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(
    AsyncAttrs, DeclarativeBase
):
    id: Mapped[uuid.UUID] = mapped_column()
