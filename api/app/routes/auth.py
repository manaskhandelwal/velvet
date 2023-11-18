from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.emails import send_otp_email
from utils.helpers import get_db, is_duplicate
from utils.errors import duplicate_error

from core.security import generate_otp, get_password_hash, create_access_token
from models.user import User 
from schemas.user import UserCreateDto

router = APIRouter()
database = Annotated[Session, Depends(get_db)]

@router.post("/register")
async def register(
    *,
    db: database,
    dto: UserCreateDto,
):

    if (
        await is_duplicate(db,User, User.email, dto.email)
    ):
        raise duplicate_error(target="email", msg="Another account is using the same email.")
    
    if (
        await is_duplicate(db,User, User.username, dto.username)
    ):
        raise duplicate_error(target="username", msg="This username isn't available. Please try another.")
    
    email_otp = generate_otp()

    user = User(
        email=dto.email,
        full_name=dto.full_name,
        username=dto.username,
        hashed_password=get_password_hash(dto.password),
        email_otp=email_otp,
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    
    await send_otp_email({"name": dto.full_name, "email": dto.email}, email_otp)

    return {"access_token": create_access_token(user.id), "access_type": "bearer"}
