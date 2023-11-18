from sqlalchemy.orm import Session
from models.user import User 



async def get_user_by_id(db: Session, id: str):
    return db.query(User).filter(User.id == id).first()

