import uuid

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from services.exceptions import UnauthException
from services.issue_tokens import get_current_token_payload
from services import users as users_service
from src import utils
from src.models import User
from src.models.db_helper import db_helper
from src.schemas.users import InfoUserSchema, LogInUserSchema


async def validate_auth_user(session: AsyncSession, user_info: LogInUserSchema):
    if not (
        db_user := await users_service.get_user_by_username(
            session=session, username=user_info.username
        )
    ):
        raise UnauthException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid username or password"
        )
    if not utils.validate_password(
        password=user_info.password, hashed_password=db_user.password
    ):
        raise UnauthException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid username or password"
        )
    return db_user


async def get_current_auth_user(
    session: AsyncSession = Depends(db_helper.session_dependency),
    payload: dict = Depends(get_current_token_payload),
) -> InfoUserSchema:
    id: uuid | None = payload.get("sub")
    if not (user := await users_service.get_user_by_id(session=session, user_id=id)):
        raise UnauthException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalid"
        )
    return user
