import boto3
from botocore.config import Config
from typing import Annotated, Any, Generator
from sqlalchemy import Column
from sqlalchemy.orm import Session
from fastapi import Depends
from core.config import settings
from db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


aws_config = Config(
    region_name=settings.AWS_REGION_NAME,
)

database = Annotated[Session, Depends(get_db)]
aws_client = boto3.client(
    "comprehend",
    config=aws_config,
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
)


async def is_duplicate(db: database, model: Any, target: Column[Any], value: str):
    model = db.query(model).filter(target == value).all()
    return len(model) != 0


def success_responce(msg: str = None):
    return {"success": True, "message": msg}


async def text_sentiment(text: str):
    response = aws_client.detect_sentiment(Text=text, LanguageCode="en")
    return response
