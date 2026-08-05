from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    gamma_api_key: str = "test_key"
    gamma_base_url: str = "https://public-api.gamma.app/v1.0"
    
    class Config:
        env_file = ".env"

settings = Settings()