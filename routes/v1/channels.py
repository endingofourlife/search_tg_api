from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database import get_db
from repository import ChannelsRepository
from schemes.dto import ChannelsDTO
from schemes.routes import CreateChannelRequest
from services import ChannelService

channels_router = APIRouter()


async def get_channel_service(session: AsyncSession = Depends(get_db)) -> ChannelService:
    return ChannelService(ChannelsRepository(session))


@channels_router.get('/{count}', response_model=list[ChannelsDTO], status_code=status.HTTP_200_OK)
async def get_channels(count: int, service: ChannelService = Depends(get_channel_service)):
    result = await service.get_channels(count)
    return result


@channels_router.post('/', response_model=ChannelsDTO, status_code=status.HTTP_201_CREATED)
async def create_channel(request: CreateChannelRequest, service: ChannelService = Depends(get_channel_service)):
    result = await service.create_channel(request)
    return result

