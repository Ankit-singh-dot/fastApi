from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import User
from app.services.user_service import *


router = APIRouter(prefix="/users")
@router.post("/")
async def create_user(user:User):
    return await create_user_service(user)

@router.get("/")
async def get_users():
    return await get_all_users_service()

@router.get("/{user_id}")
async def get_user(user_id:int):
    user = await get_user_service(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found ")
    return  user


@router.delete("/{user_id}")
async def delete_user(user_id:int):
    user = await delete_user_service(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found ")
    return  {"message": "Deleted"}