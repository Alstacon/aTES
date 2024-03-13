from pydantic import BaseModel

from src.models.users import UserRoles


class AddUserSchema(BaseModel):
    username: str
    email: str
    role: UserRoles = UserRoles.EMPLOYEE
    password: bytes


class UpdateUserSchema(BaseModel):
    role: UserRoles


class InfoUserSchema(AddUserSchema):
    id: int
    public_id: str


class PubIDUserSchema(BaseModel):
    public_id: str
