from app.database.fake_db import book_db

async def create_book_services(book):
    book_db.append(book)
    return book

async def getAllBook_services():
    return book_db

async def getBookById_services(book_id):
    for book in book_db:
        if book.id == book_id:
            return book
    return None


async def deleteBookById_services(book_id):
    for book in book_db:
        if book.id == book_id:
            book_db.remove(book)
            return book 
    return None
