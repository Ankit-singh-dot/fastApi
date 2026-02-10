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


async def updateBook_put_services(book_id, updated_book):
    for book in book_db:
        if book.id == book_id:
            book.title = updated_book.title
            book.author = updated_book.author
            book.price = updated_book.price
            return book
    return None

async def updateBook_patch_services(book_id, updated_book):
    for book in book_db:
        if book.id == book_id:

            if updated_book.title is not None:
                book.title = updated_book.title

            if updated_book.author is not None:
                book.author = updated_book.author

            if updated_book.price is not None:
                book.price = updated_book.price

            return book
    return None