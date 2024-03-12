import datetime
import uuid
from datetime import timedelta

import jwt
from jwt.exceptions import InvalidTokenError
import bcrypt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette import status

from config import settings

def get_public_id() -> str:
    return uuid.uuid4().hex


def hash_password(
        password: str
) -> bytes:
    salt = bcrypt.gensalt()
    password_bytes = password.encode()
    return bcrypt.hashpw(password_bytes, salt)


def validate_password(
        password: str,
        hashed_password: bytes
) -> bool:
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password
    )
