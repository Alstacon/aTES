import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import User
from src.models.db_helper import db_helper
from src.models.users import UserRoles
from src.schemas.users import AddUserSchema
from src.utils import hash_password


async def create_user(session: AsyncSession, user_data: AddUserSchema) -> User:
    new_password = hash_password(user_data.password)
    user_data.password = new_password.decode()
    user = User(**user_data.model_dump())
    session.add(user)
    await session.commit()
    return user


async def update_user_role(
    session: AsyncSession, user: User, new_role: UserRoles
) -> User: ...


async def get_user_by_id(session: AsyncSession, user_id: int) -> User:
    stmt = select(User).where(User.id == user_id)
    user: User | None = await session.scalar(stmt)
    print(user)
    return user

