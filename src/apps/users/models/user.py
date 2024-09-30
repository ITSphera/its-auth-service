from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from common.models import Base


class BaseUserModel:
    """Base user model."""

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        Integer, nullable=False, unique=True, autoincrement=True, primary_key=True
    )
    username: Mapped[str] = mapped_column(
        String(length=64), unique=True, index=True, nullable=True
    )
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    is_banned: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)


class UserModel(BaseUserModel, Base):
    __tablename__ = "users"

    display_name: Mapped[str] = mapped_column(String(length=64), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(length=16), nullable=True)
    country: Mapped[str] = mapped_column(String(length=30), nullable=True)
    city: Mapped[str] = mapped_column(String(length=35), nullable=True)
    first_name: Mapped[str] = mapped_column(String(15), nullable=True)
    last_name: Mapped[str] = mapped_column(String(15), nullable=True)
    bio: Mapped[str] = mapped_column(String(length=2000), default="", nullable=True)
    avatar_url: Mapped[str] = mapped_column(
        String(length=150), nullable=True
    )  # найти дефолт урл ту аватар пользователя

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_default_values()

    def __repr__(self):
        return f"UserModel(id={self.id}, username={self.username})"

    def __str__(self):
        return f"{self.username}"

    def _generate_default_username(self):
        return f"username_{self.id}"

    def set_default_values(self):
        if not self.username:
            self.username = self._generate_default_username()
        if not self.display_name:
            self.display_name = self.username
