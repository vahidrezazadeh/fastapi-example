from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    tags=["Login Api"],
    prefix='/login'
    )


@router.post("/", response_model=str)
def loginUser():
    return "Login User API Response"