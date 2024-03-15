from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from services.exceptions import UserAlreadyExists
from services.identify_users import get_current_auth_user
from services.users import create_user as create_user_service
from src.models import User
from src.models.db_helper import db_helper
from src.schemas.users import InfoUserSchema, AddUserSchema

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=InfoUserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: AddUserSchema,
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> User:
    if not (user := await create_user_service(session=session, user_data=user_data)):
        raise UserAlreadyExists(
            status_code=status.HTTP_409_CONFLICT, detail="User already exists"
        )
    return user


@router.get("/me/")
def auth_user_info(user: InfoUserSchema = Depends(get_current_auth_user)):
    return {
        "username": user.username,
        "email": user.email,
    }
