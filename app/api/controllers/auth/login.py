from fastapi import APIRouter, Depends, HTTPException

from app.schemas.auth.LoginSchema import LoginSchema

from services.AuthService import AuthService

router = APIRouter(
    tags=["Login Api"],
    prefix='/login'
    )


@router.post("/", response_model=dict)
async def loginUser(body : LoginSchema):
    print(body)
    userId = 1
    jwtData =await AuthService.generateTokens(userId)
    return jwtData