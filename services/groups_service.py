from services.base import BaseService, T, U
from repository import GroupsRepository


class GroupService(BaseService):
    def __init__(self, repository: GroupsRepository):
        super().__init__()
        self._repository = repository

    def _convert_to_dto(self, model: T) -> U:
        pass

    async def get_groups(self, count: int) -> list[U]:
        pass

    async def create_group(self, group: U) -> U:
        pass