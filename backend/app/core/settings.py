from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables.

    Uses Pydantic Settings to support .env files and environment overrides.
    """

    app_name: str = "ECHO Backend"
    env: str = "development"

    database_url: str = "postgresql://echo:echo_password@db:5432/echo"
    redis_url: str = "redis://redis:6379/0"

    secret_key: str = "change-this-in-prod"
    access_token_expire_minutes: int = 60

    model_config = SettingsConfigDict(env_file=".env", env_prefix="", extra="ignore")


settings = Settings()


