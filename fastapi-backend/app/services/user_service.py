from app.database.fake_db import user_db

async def create_user_service(user):
    user_db.append(user)
    return user

async def get_all_users_service():
    return user_db


async def get_user_service(user_id):
    for user in user_db:
        if user.id == user_id:
            return user
    return None

async def delete_user_service(user_id):
    for user in user_db:
        if user.id == user_id:
            user_db.remove(user)
            return user
    return None