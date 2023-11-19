from pyexpat import model
from typing import Annotated, Any, Generator
from sqlalchemy import Column
from sqlalchemy.orm import Session
from fastapi import Depends
from db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

database = Annotated[Session, Depends(get_db)]


async def is_duplicate(db: database, model: Any , target: Column[Any], value: str):
    model = db.query(model).filter(target == value).all()
    return len(model) != 0


def success_responce(msg: str = None):
    return {"success": True, "message": msg}