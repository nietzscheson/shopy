from pydantic import BaseModel


class UserScheme(BaseModel):
    name: str
