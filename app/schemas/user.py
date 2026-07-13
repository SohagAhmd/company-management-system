from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class Response_model(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True
