from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://user:password@localhost:5432/afde"
    openai_api_key: str = "mock-key"
    model_name: str = "mock-model"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
