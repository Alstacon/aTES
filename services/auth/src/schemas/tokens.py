from pydantic import BaseModel


class InfoTokenSchema(BaseModel):
    access_token: str
    token_type: str