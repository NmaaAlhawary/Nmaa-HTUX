# app/DB/__init__.py
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from .database import Base, AsyncSessionLocal

# Import all model modules for automatic registration
from .models import user , todo

@asynccontextmanager
async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """Provides an asynchronous database session for FastAPI."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()