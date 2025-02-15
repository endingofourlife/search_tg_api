from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database import get_db
from repository import GroupsRepository
from schemes.dto import GroupsDTO
from schemes.routes import CreateGroupRequest
from services import GroupService

groups_router = APIRouter()


async def get_groups_service(session: AsyncSession = Depends(get_db)) -> GroupService:
    return GroupService(GroupsRepository(session))


@groups_router.get('/{count}', response_model=list[GroupsDTO], status_code=status.HTTP_200_OK)
async def get_groups(count: int, service: GroupService = Depends(get_groups_service)):
    result = await service.get_groups(count)
    return result


@groups_router.post('/', response_model=GroupsDTO, status_code=status.HTTP_201_CREATED)
async def create_group(request: CreateGroupRequest, service: GroupService = Depends(get_groups_service)):
    result = await service.create_group(request)
    return result

