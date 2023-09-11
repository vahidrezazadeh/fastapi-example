from pydantic_settings import BaseSettings

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

    class Config:
        env_file = ".env"

settings = Settings()