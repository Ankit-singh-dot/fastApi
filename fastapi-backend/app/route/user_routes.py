from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import Books
from app.services.user_service import *


router = APIRouter(prefix="/book")
@router.post("/")
async def create_book(book:Books):
    return await create_book_services(book)

@router.get("/")
async def getAllBook():
    return await getAllBook_services()

@router.get("/{book_id}")
async def get_user(book_id:int):
    user = await getBookById_services(book_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found ")
    return  user


@router.delete("/{book_id}")
async def delete_user(book_id:int):
    user = await deleteBookById_services(book_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found ")
    return  {"message": "Deleted"}