from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    app_name: str = "Fast Api Project Name"
    debug: bool = True
    secret_key: str = ''
    apiPrefix  : str = "api"
    apiVersion : str = "v1"
    ALLOWED_HOSTS : list = []

    DATETIME_TIMEZONE: str = 'Asia/Tehran'
    DATETIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'

    LOG_STDOUT_FILENAME: str = 'fapi_log_access.log'
    LOG_STDERR_FILENAME: str = 'fapi_log_error.log'

    TOKEN_EXPIRE_SECONDS : int = 86400 # Expiration time, unit: seconds ( 86400 = 1 * 24 * 60 * 60)
    TOKEN_SECRET_KEY : str = 'jwt_secret_key'
    TOKEN_ALGORITHM : str = 'HS256'

    class Config:
        env_file = ".env"

settings = Settings()