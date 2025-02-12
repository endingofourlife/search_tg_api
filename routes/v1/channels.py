from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database import get_db
from repository import ChannelsRepository
from services import ChannelService

channels_router = APIRouter()

async def get_channel_service(session: AsyncSession = Depends(get_db)) -> ChannelService:
    return ChannelService(ChannelsRepository(session))

@channels_router.get('/{count}', response_model=None, status_code=status.HTTP_200_OK)
async def get_channels(count: int, service: ChannelService = Depends(get_channel_service)):
    return {'count': count}

@channels_router.post('/', response_model=None, status_code=status.HTTP_201_CREATED)
async def create_channel(request: None, service: ChannelService = Depends(get_channel_service)):
    return {'status': 'ok'}
