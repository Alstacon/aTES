import uuid
import jwt
import bcrypt
from config import settings


def get_public_id() -> str:
    return uuid.uuid4().hex


def encode_jwt(
        payload: dict,
        private_key: str = settings.auth_jwt.private_key_path.read_text(),
        algorithm: str = settings.auth_jwt.algorithm,
):
    encoded = jwt.encode(payload, private_key, algorithm)
    return encoded


def decode_jwt(
        token: str | bytes,
        public_key: str = settings.auth_jwt.public_key_path.read_text(),
        algotithm: str = settings.auth_jwt.algorithm,
):
    decoded = jwt.decode(token, public_key, algorithms=[algotithm])
    return decoded


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
