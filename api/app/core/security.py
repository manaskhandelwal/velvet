from datetime import datetime, timedelta
from random import randint
from typing import Annotated, Any, Union
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.hash import argon2
from jose import JWTError, jwt

from utils.errors import unauthorized_error
from .config import settings


oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, settings.ACCESS_TOKEN_SECRET_KEY, settings.ACCESS_TOKEN_ALGORITHM)
        user_id: str = payload.get("sub")

        if user_id is None:
            raise unauthorized_error("user-id")

        return {"id": user_id}

    except JWTError:
        raise unauthorized_error("JWTError")


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.ACCESS_TOKEN_SECRET_KEY, algorithm=settings.ACCESS_TOKEN_ALGORITHM)

    return encoded_jwt


def generate_otp(n: int = 6) -> int:
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def get_password_hash(password: str) -> str:
    return argon2.using(rounds=10).hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return argon2.verify(plain_password, hashed_password)
