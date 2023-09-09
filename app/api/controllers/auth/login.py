from fastapi import APIRouter, Depends, HTTPException

from app.schemas.auth.LoginSchema import LoginSchema

router = APIRouter(
    tags=["Login Api"],
    prefix='/login'
    )


@router.post("/", response_model=str)
def loginUser(body : LoginSchema):
    print(body)
    return "Login User API Response"