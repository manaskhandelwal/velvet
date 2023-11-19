from sqlalchemy.orm import Session
from models.moment import Moment 



async def get_moment_by_id(db: Session, id: str):
    return db.query(Moment).filter(Moment.id == id).first()
