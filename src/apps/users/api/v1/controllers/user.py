from fastapi.exceptions import HTTPException
from modules.auth import get_password_hash
from modules.responses.user import responses as user_responses
from fastapi import APIRouter, status
from core.dao import UserDAO
from fastapi.responses import JSONResponse
from fastapi.responses import Response
from schemas.user import CreateUserSchema

user_router = APIRouter(prefix="/api/v1/profile", tags=["Profile"])


@user_router.post(path="/register", summary="Регистрация пользователя")
async def create_user(registration_user_data: CreateUserSchema) -> JSONResponse:
    user = await UserDAO.get_one_or_none(registration_user_data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=user_responses.USER_ALREADY_EXISTS,
        )

    registration_user_data.password_1 = get_password_hash(registration_user_data.password_1)
    new_user = await UserDAO.add(registration_user_data)
    return JSONResponse(status_code=201, content=f"Успешно. Вот юзер: {new_user}")
