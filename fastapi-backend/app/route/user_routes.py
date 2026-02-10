from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import *
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

@router.put("/{book_id}")
async def update_book_put(book_id: int, book: UpdateBookPut):
    updated = await updateBook_put_services(book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated


@router.patch("/{book_id}")
async def update_book_patch(book_id: int, book: UpdateBookPatch):
    updated = await updateBook_patch_services(book_id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated



# sql alchemy is the most popular orm for python mapping object to database tables and providing a high-level SQL language 