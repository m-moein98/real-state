from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    userId: str


class User(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    username: str
    fullName: Optional[str]
    email: str
    password: str
    DoB: Optional[datetime]
    gender: Optional[str]
    createdAt: datetime = datetime.utcnow()
    updatedAt: datetime = datetime.utcnow()
