from api.endpoints import users
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(users.router)