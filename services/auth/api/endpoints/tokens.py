from fastapi import APIRouter, Depends

from src import utils
from src.schemas.tokens import InfoTokenSchema
from src.schemas.users import InfoUserSchema

router = APIRouter(prefix='/jwt', tags=['JWT'])


@router.post('/login/', response_model=InfoTokenSchema)
def auth_user_issue_jwt(
        user: InfoUserSchema = Depends(),

):
    jwt_payload = {
        'sub': user.id,
        'username': user.username,
        'email': user.email,
    }
    token = utils.encode_jwt(payload=jwt_payload)
    return InfoTokenSchema(
        access_token=token,
        token_type='Bearer'
    )
