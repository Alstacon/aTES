from pydantic import BaseModel

from src.models import UserRoles


class AddUserSchema(BaseModel):
    username: str
    email: str
    role: UserRoles = UserRoles.EMPLOYEE
    password: bytes


class UpdateUserSchema(BaseModel):
    role: UserRoles


class InfoUserSchema(BaseModel):
    id: int
    public_id: str
    username: str
    email: str
    role: UserRoles


class PubIDUserSchema(BaseModel):
    public_id: str
