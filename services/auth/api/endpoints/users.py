from fastapi import APIRouter, Depends

from services.identify_users import get_current_auth_user
from src.schemas.users import InfoUserSchema

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/me/')
def auth_user_info(
        user: InfoUserSchema = Depends(get_current_auth_user)
):
    return {
        'username': user.username,
        'email': user.email,
    }
