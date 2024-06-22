from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.settings import settings


engine = create_async_engine(settings.postgres_url)
postgres_session_factory = async_sessionmaker(engine, expire_on_commit=False)
