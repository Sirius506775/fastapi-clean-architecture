from fastapi import APIRouter
from pydantic import BaseModel
from user.application.user_service import UserService

# API Router 객체 생성
router = APIRouter(prefix="/users", tags=["user"])


class CreateUserBody(BaseModel):
    name: str
    email: str
    password: str


# path operation functions
@router.post("/", status_code=201)
def create_user(user: CreateUserBody):
    user_service = UserService()
    create_user = user_service.create_user(
        user.name,
        user.email,
        user.password,
    )

    return create_user
