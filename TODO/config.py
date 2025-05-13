# config.py
from enum import Enum

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Configs(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('.env', '.env.prod'),
        env_file_encoding='utf-8',
        extra='ignore'
    )



    ENVIRONMENT: str = 'development'  # Default value
    DATABASE_URL: str


configs = Configs()
