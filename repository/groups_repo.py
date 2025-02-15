from sqlalchemy import select

from database.models import Group
from repository.base import BaseRepo


class GroupsRepository(BaseRepo):
    async def get_all_groups(self, limit: int = 10):
        result = await self._db_session.execute(
            select(Group)
            .order_by(Group.sub_count.desc())
            .limit(limit)
        )
        return result.scalars().all()

    async def create_group(self, url: str, sub_count: int, key_word: str) -> Group:
        group = Group(url=url, sub_count=sub_count, key_word=key_word)
        self._db_session.add(group)
        await self._db_session.commit()
        return group
