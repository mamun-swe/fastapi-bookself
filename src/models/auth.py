
from pydantic import BaseModel, EmailStr


class Login(BaseModel):
    name: str
    email: EmailStr
