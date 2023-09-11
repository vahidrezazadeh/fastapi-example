from utils.timezones import timezone_utils
from datetime import datetime, timedelta
from settings import settings
from jose import jwt


async def create_access_token(sub: str, expires_delta: timedelta | None = None, **kwargs) -> tuple[str, datetime]:
    """
    Generate encryption token

    :param sub: The subject/userid of the JWT
    :param expires_delta: Increased expiry time
    :return:
    """
    if expires_delta:
        expire = timezone_utils.get_timezone_expire_time(expires_delta)
    else:
        expire = timezone_utils.get_timezone_expire_time(timedelta(seconds=settings.TOKEN_EXPIRE_SECONDS))
    to_encode = {'exp': expire, 'sub': sub, **kwargs}
    token = jwt.encode(to_encode, settings.TOKEN_SECRET_KEY, settings.TOKEN_ALGORITHM)
    
    return token, expire


async def create_refresh_token(sub: str, expire_time: datetime | None = None, **kwargs) -> tuple[str, datetime]:
    """
    Generate encryption refresh token, only used to create a new token

    :param sub: The subject/userid of the JWT
    :param expire_time: expiry time
    :return:
    """
    if expire_time:
        expire = expire_time + timedelta(seconds=settings.TOKEN_REFRESH_EXPIRE_SECONDS)
    else:
        expire = timezone_utils.get_timezone_expire_time(timedelta(seconds=settings.TOKEN_EXPIRE_SECONDS))
    to_encode = {'exp': expire, 'sub': sub, **kwargs}
    refresh_token = jwt.encode(to_encode, settings.TOKEN_SECRET_KEY, settings.TOKEN_ALGORITHM)
   
    return refresh_token, expire

async def jwt_decode(refresh_token : str):
    """
    Decode token

    :param token:
    :return:
    """
    try:
        payload = jwt.decode(refresh_token, settings.TOKEN_SECRET_KEY, algorithms=[settings.TOKEN_ALGORITHM])
        user_id = int(payload.get('sub'))
        if not user_id:
            raise Exception("Token Is Not Valid")
    except :
        raise Exception("Error on Decode Token")
    return user_id

