from sqlalchemy.ext.asyncio import AsyncSession

from core import LoggerConfig


class BaseRepo:
    def __init__(self, db_session: AsyncSession):
        self._db_session = db_session
        self._logger = LoggerConfig.get_logger(__name__)

    async def commit(self):
        await self._db_session.commit()

    async def rollback(self):
        await self._db_session.rollback()