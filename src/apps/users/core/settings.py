import os
from functools import lru_cache

from dotenv import load_dotenv


class ServerSettings:
    def __init__(self):
        self.HOST = os.environ.get("SERVER_HOST")
        self.PORT = int(os.environ.get("SERVER_PORT"))


class DatabaseSettings:
    def __init__(self):
        load_dotenv()
        self.DATABASE_NAME = os.environ.get("DATABASE_NAME")
        self.DATABASE_USER = os.environ.get("DATABASE_USER")
        self.DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
        self.DATABASE_HOST = os.environ.get("DATABASE_HOST")
        self.DATABASE_PORT = os.environ.get("DATABASE_PORT")

        self.DRIVER = os.environ.get("DATABASE_DRIVER")
        self.DATABASE = os.environ.get("DATABASE")

        self.DATABASE_URL = (
            f"{self.DATABASE}+{self.DRIVER}://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}"
            f"/{self.DATABASE_NAME}"
        )


class HashingSettings:
    def __init__(self):
        self.SECRET_KEY = os.environ.get("SECRET_KEY")
        self.ALGORITHM = os.environ.get("ALGORITHM")

@lru_cache
def get_database_settings():
    return DatabaseSettings()

@lru_cache
def get_server_settings():
    return ServerSettings()

@lru_cache
def get_auth_data():
    return HashingSettings()


database_settings = get_database_settings()
server_settings = get_server_settings()
hash_settings = get_auth_data()
