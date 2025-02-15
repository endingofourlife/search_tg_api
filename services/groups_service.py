from database.models import Group
from schemes.dto import GroupsDTO
from schemes.routes import CreateGroupRequest
from services.base import BaseService
from repository import GroupsRepository


class GroupService(BaseService):
    def __init__(self, repository: GroupsRepository):
        super().__init__()
        self._repository = repository

    def _convert_to_dto(self, model: Group) -> GroupsDTO:
        return GroupsDTO(
            url=model.url,
            sub_count=model.sub_count
        )

    async def get_groups(self, count: int) -> list[GroupsDTO]:
        """Fetches a list of groups with a specified limit."""
        self._logger.info(f'Fetching groups. Requested count: {count}')
        try:
            result = await self._repository.get_all_groups(limit=count)
            self._logger.info(f'Successfully fetched {len(result)} groups.')
            return [self._convert_to_dto(group) for group in result]
        except Exception as e:
            self._logger.error(f'Failed to fetch groups. Error: {str(e)}', exc_info=True)
            return []  # Return an empty list in case of an error

    async def create_group(self, request: CreateGroupRequest) -> GroupsDTO | None:
        """Creates a new group based on the provided request."""
        self._logger.info(f'Creating a new group. Request details: {request}')
        try:
            result = await self._repository.create_group(
                url=request.url,
                sub_count=request.sub_count,
                key_word=request.key_word
            )
            self._logger.info(f'Successfully created group with URL: {request.url}')
            return self._convert_to_dto(result)
        except Exception as e:
            self._logger.error(f'Failed to create group. Error: {str(e)}', exc_info=True)
            return None
