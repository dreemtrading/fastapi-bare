# all configurations will go in to this class
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    DB_CONN: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PWD: str

    model_config = SettingsConfigDict(
        env_file=DOTENV,
        # extra='ignore'
    )


Config = Settings()
