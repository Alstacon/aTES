from fastapi import HTTPException
from starlette import status


class UserAlreadyExists(HTTPException): ...


class UnauthException(HTTPException): ...
