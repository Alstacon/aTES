import uuid

from fastapi import Depends

from services.issue_tokens import get_current_token_payload
from src.schemas.users import InfoUserSchema


def get_current_auth_user(
        payload: dict = Depends(get_current_token_payload),
) -> InfoUserSchema:
    id: uuid | None = payload.get('sub')
    ...
