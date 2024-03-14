from pydantic import BaseModel

from src.models.users import UserRoles


class UserSchema(BaseModel):
    username: str
    email: str
    role: UserRoles = UserRoles.EMPLOYEE
    password: bytes


class AddUserSchema(UserSchema):
    password: str


class LogInUserSchema(BaseModel):
    username: str
    password: str


class UpdateUserSchema(BaseModel):
    role: UserRoles


class InfoUserSchema(UserSchema):
    id: int
    public_id: str


class PubIDUserSchema(BaseModel):
    public_id: str
