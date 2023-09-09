from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Fast Api Project Name"
    debug: bool = True
    secret_key: str = ''
    apiPrefix  : str = "api"
    apiVersion : str = "v1"
    ALLOWED_HOSTS : list = []

    class Config:
        env_file = ".env"

settings = Settings()