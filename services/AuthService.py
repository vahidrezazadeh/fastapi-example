from utils.jwt import create_access_token , create_refresh_token ,jwt_decode
from datetime import datetime


class AuthService:
    @staticmethod
    async def generateTokens(user_id : int) -> dict: 

        access_token, access_token_expire_time = await create_access_token(
                    str(user_id), multi_login=False
                )
        
        refresh_token, refresh_token_expire_time = await create_refresh_token(
                    str(user_id), multi_login=False
                )
        
        return {
            "access_token": access_token,
            "access_token_expire" : access_token_expire_time,
            "refresh_token": refresh_token,
            "refresh_token_expire" : refresh_token_expire_time,
        }
    
    @staticmethod
    async def generateNewAccessToken(*, refresh_token: str) -> tuple[str, datetime]:
        user_id = await jwt_decode(refresh_token)
        access_new_token, access_new_token_expire_time = await create_access_token(
                str(user_id), refresh_token, multi_login=False
            )
        return access_new_token, access_new_token_expire_time
            