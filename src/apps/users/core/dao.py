import asyncio
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import async_session_maker
from models import UserModel


class BaseDAO:
    model = None

    # @classmethod
    # async def get_one_or_none(cls):
    #     async with async_sessionmaker() as session:
    #         query = select


class UserDAO(BaseDAO):
    model = UserModel

    @classmethod
    async def get_one_or_none(cls, email: str) -> Optional[UserModel]:
        async with async_session_maker() as session:
            session: AsyncSession
            query = select(cls.model).where(cls.model.email == email)
            query_result = await session.execute(query)
            # Используем scalar_one_or_none для получения объекта модели или None
            user = query_result.scalar_one_or_none()
            return user

    @classmethod
    async def add(cls, **user_data: dict):
        async with async_session_maker() as session:
            session: AsyncSession
            new_user = UserModel(**user_data)
            session.add(new_user)
            await session.commit()
            return new_user


async def main():
    result = await UserDAO.get_one_or_none("")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
