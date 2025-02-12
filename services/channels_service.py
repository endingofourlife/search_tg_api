from repository import ChannelsRepository
from services.base import BaseService, T, U


class ChannelService(BaseService):
    def __init__(self, repository: ChannelsRepository):
        super().__init__()
        self._repository = repository

    def _convert_to_dto(self, model: T) -> U:
        pass

    async def get_channels(self, count: int) -> U:
        pass

    async def create_channel(self, request: None) -> U:
        pass
