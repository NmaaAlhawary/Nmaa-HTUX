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

    # Pricing per 1K tokens for different models
    open_ai_pricing: dict = {
        "gpt-4o": {"input": 0.005, "output": 0.015},
        "gpt-4o-mini": {"input": 0.000150, "output": 0.000600},
        "gpt-4-turbo": {"input": 0.01, "output": 0.03},
        "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
        "whisper-1": {"cost_per_minute": 0.006}
    }

    ENVIRONMENT: str = 'development'  # Default value
    ENCRYPTION_KEY: str
    SECRET_TOKEN_ENCRYPTION_KEY: str

    OPENAI_KEY: str
    OPENAI_PROJECT_ID: str
    OPENAI_ORG_ID: str

    SYSTEM_ID: str
    API_KEY_NAME: str = 'X-API-KEY'
    API_KEY: str

    DATABASE_URL: str
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str

    # Email Service

    SMTP_SERVER: str
    SMTP_PORT: str
    EMAIL: str
    PASSWORD: str

    API_V1_STR: str = '/api/v1'

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    HTUX_SITE_BASE_URL: str
    WORDPRESS_API_ENDPOINT: str
    WP_API_KEY: str

    UPDATE_STUDENTS_JOB_INTERVAL: int = 0
    UPDATE_REPORTING_USERS_JOB_INTERVAL: int = 0
    UPDATE_CERTIFICATES_JOB_INTERVAL: int = 0

    ACCREDIBLE_API_KEY: str

configs = Configs()
