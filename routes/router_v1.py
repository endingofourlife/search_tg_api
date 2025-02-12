from fastapi import APIRouter

from routes.v1 import channels_router, groups_router

api_v1_router = APIRouter()
api_v1_router.include_router(channels_router, prefix='/channels', tags=['channels endpoints'])
api_v1_router.include_router(groups_router, prefix='/groups', tags=['groups endpoints'])

