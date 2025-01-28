from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.database import async_session_maker


async def get_session_with_commit() -> AsyncGenerator[AsyncSession, None]:
    """Асинхронная сессия с автоматическим коммитом."""
    async with async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e  # Явно поднимаем исключение для лучшей отладки


async def get_session_without_commit() -> AsyncGenerator[AsyncSession, None]:
    """Асинхронная сессия без автоматического коммита."""
    async with async_session_maker() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e  # Явно поднимаем исключение для лучшей отладки
