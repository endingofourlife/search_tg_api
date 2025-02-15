from typing import Sequence

from sqlalchemy import select

from database.models import Channel
from repository.base import BaseRepo


class ChannelsRepository(BaseRepo):
    async def get_all_channels(self, limit: int = 10) -> Sequence[Channel]:
        result = await self._db_session.execute(
            select(Channel)
            .order_by(Channel.sub_count.desc())
            .limit(limit)
        )
        return result.scalars().all()

    async def create_channel(self, url: str, sub_count: int, key_word: str) -> Channel:
        channel = Channel(url=url, sub_count=sub_count, key_word=key_word)
        self._db_session.add(channel)
        await self._db_session.commit()
        return channel
