from sqlalchemy.orm import Session
from utils.errors import not_found_error
from core.security import verify_password
from models.user import User 



async def get_user_by_id(db: Session, id: str):
    return db.query(User).filter(User.id == id).first()


async def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


async def authenticate_user(db: Session, username: str, password: str):
    user: User = await get_user_by_username(db, username)

    if user is None or not verify_password(password, user.hashed_password):
        raise not_found_error("user", "Invalid Details")

    return user
