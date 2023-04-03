from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from ..core.config import settings

DATABASE_URI = settings.ASYNC_TEST_DATABASE_URI

async_engine = create_async_engine(
    DATABASE_URI,
    echo=False,
    future=True,
    pool_size=settings.POOL_SIZE,
    max_overflow=64,
)

async_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
