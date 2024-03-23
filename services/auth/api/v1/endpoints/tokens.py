from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services import issue_tokens
from services.identify_users import validate_auth_user
from src.models.db_helper import db_helper
from src.schemas.tokens import InfoTokenSchema
from src.schemas.users import LogInUserSchema, UserSchema

router = APIRouter()


@router.post("/login/", response_model=InfoTokenSchema)
async def auth_user_issue_jwt(
    user: LogInUserSchema = Depends(validate_auth_user),
):
    jwt_payload = {
        "sub": user.id,
        "username": user.username,
        "email": user.email,
    }
    token = issue_tokens.encode_jwt(payload=jwt_payload)
    return InfoTokenSchema(access_token=token, token_type="Bearer")
