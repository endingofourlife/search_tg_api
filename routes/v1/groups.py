from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database import get_db
from repository import GroupsRepository
from services import GroupService

groups_router = APIRouter()

async def get_groups_service(session: AsyncSession = Depends(get_db)) -> GroupService:
    return GroupService(GroupsRepository(session))

@groups_router.get('/{count}', response_model=None, status_code=status.HTTP_200_OK)
async def get_group(count: int, service: GroupService = Depends(get_groups_service)):
    return {'count': count}

@groups_router.post('/', response_model=None, status_code=status.HTTP_201_CREATED)
async def create_group(request: None, service: GroupService = Depends(get_groups_service)):
    return {'status': 'ok'}
