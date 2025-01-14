import os
from typing import List
from loguru import logger


from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    FORMAT_LOG: str = (
        "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {name}:{function}:{line} - {message}"
    )
    LOG_ROTATION: str = "10 MB"
    DB_URL: str = "sqlite+aiosqlite:///data/db.sqlite3"
    
    SECRET_KEY: str
    ALGORITHM: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    # REDIS_PASSWORD: str
    # REDIS_USER: str


    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )

    def get_redis_url(self):
        return (
            f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
        )

    def get_db_url(self):
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


# Получаем параметры для загрузки переменных среды
settings = Settings()


log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.log")
logger.add(
    log_file_path,
    format=settings.FORMAT_LOG,
    level="INFO",
    rotation=settings.LOG_ROTATION,
)
DATABASE_LITE_URL = settings.DB_URL

DATABASE_PG_URL = settings.get_db_url()
REDIS_URL = settings.get_redis_url()
