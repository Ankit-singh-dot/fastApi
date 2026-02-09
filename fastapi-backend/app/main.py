from fastapi import FastAPI
from app.route.user_routes import router as user_router

app = FastAPI()

app.include_router(user_router)