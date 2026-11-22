from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Inventory Management API"
    APP_ENV: str = "development"
    DEBUG: bool = True

    API_V1_PREFIX: str =  "/api/v1"

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        case_sensitive = True,
        extra = "ignore"
    )

settings = Settings()