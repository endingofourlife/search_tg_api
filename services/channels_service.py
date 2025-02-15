from database.models import Channel
from repository import ChannelsRepository
from schemes.dto import ChannelsDTO
from schemes.routes import CreateChannelRequest
from services.base import BaseService


class ChannelService(BaseService):
    def __init__(self, repository: ChannelsRepository):
        super().__init__()
        self._repository = repository

    def _convert_to_dto(self, model: Channel) -> ChannelsDTO:
        return ChannelsDTO(
            url=model.url,
            sub_count=model.sub_count
        )

    async def get_channels(self, count: int) -> list[ChannelsDTO]:
        self._logger.info(f'Fetching channels. Requested count: {count}')
        try:
            result = await self._repository.get_all_channels(limit=count)
            self._logger.info(f'Successfully fetched {len(result)} channels.')
            return [self._convert_to_dto(channel) for channel in result]
        except Exception as e:
            self._logger.error(f'Failed to fetch channels. Error: {str(e)}', exc_info=True)
            return []

    async def create_channel(self, request: CreateChannelRequest) -> ChannelsDTO | None:
        self._logger.info(f'Creating a new channel. Request details: {request}')
        try:
            result = await self._repository.create_channel(
                url=request.url,
                sub_count=request.sub_count,
                key_word=request.key_word
            )
            self._logger.info(f'Successfully created channel with URL: {request.url}')
            return self._convert_to_dto(result)
        except Exception as e:
            self._logger.error(f'Failed to create channel. Error: {str(e)}', exc_info=True)
            return None