import re

from email_validator import EmailNotValidError
from pydantic import BaseModel, field_validator, EmailStr, Field, validator
from modules.responses.user import responses as user_responses
from email_validator.validate_email import validate_email


from modules.special_text import SPECIAL_SYMBOLS


class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    is_banned: bool
    is_active: bool
    is_staff: bool
    is_admin: bool
    hashed_password: str
    display_name: str
    phone_number: str
    country: str
    city: str
    first_name: str
    last_name: str
    bio: str
    avatar_url: str


class CreateUserSchema(BaseModel):
    email: EmailStr | None = Field(default=None)
    password_1: str
    password_2: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        """Валидация email."""
        try:
            validate_email(value)
        except EmailNotValidError:
            raise ValueError(user_responses.NOT_VALID_EMAIL)
        return value

    @field_validator("password_1")
    @classmethod
    def validate_password_1(cls, password):
        """Валидация первого пароля."""
        pattern = (
            f"^(?=.*[a-zа-я])"  # Должна быть хотя бы одна строчная буква
            f"(?=.*[A-ZА-Я])"  # Должна быть хотя бы одна заглавная буква
            f"(?=.*[0-9])"  # Должна быть хотя бы одна цифра
            f"(?=.*[{re.escape(SPECIAL_SYMBOLS)}])"  # Должен быть хотя бы один спецсимвол
        )

        # Проверка пароля по регулярному выражению
        if not re.match(pattern, password) or len(password) < 8:
            raise ValueError(user_responses.PASSWORD_SHOULD_BE_CORRECT)

        return password

    @validator("password_2")
    def passwords_match(cls, v, values, **kwargs):
        if "password1" in values and v != values["password1"]:
            raise ValueError("passwords do not match")
        return v
