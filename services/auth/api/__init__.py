from api.v1.endpoints import users, tokens
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(tokens.router, prefix="/jwt", tags=["jwt"])
