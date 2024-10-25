from modules.special_text import SPECIAL_SYMBOLS

SUCCESSFUL_USER_REGISTER = {
    "status": 201,
    "message": "Пользователь успешно зарегистрирован.",
}
USER_ALREADY_EXISTS = {
    "status": 400,
    "message": "Пользователь с таким email уже существует.",
}
PASSWORD_SHOULD_BE_CORRECT: str = (
    "Строка, обязательный, минимум 8 символов, не может быть простым и состоять только из цифр."
)
PASSWORD_MUST_CONTAIN_SPECIAL_CHARACTER: str = (
    f"Пароль должен содержать хотя бы один специальный символ: ({SPECIAL_SYMBOLS})."
)
NOT_VALID_EMAIL: str = "Не корректный email."
PASSWORDS_ARE_NOT_EQUAL: str = "Пароли не одинаковы."
