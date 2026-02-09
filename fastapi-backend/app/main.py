from fastapi import FastAPI
from app.route.user_routes import router as book_router

app = FastAPI()

app.include_router(book_router)