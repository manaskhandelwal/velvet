from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from utils.user import authenticate_user, get_user_by_id
from utils.emails import send_otp_email
from utils.helpers import get_db, is_duplicate, success_responce
from utils.errors import duplicate_error, not_found_error

from core.security import (
    generate_otp,
    get_current_user,
    get_password_hash,
    create_access_token,
)
from models.user import User
from schemas.user import UserCreateDto, UserLoginDto, UserOtpVerifyDto


router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.post("/register")
async def register(
    db: db_dependency,
    dto: UserCreateDto,
):
    if await is_duplicate(db, User, User.email, dto.email):
        raise duplicate_error(
            target="email", msg="Another account is using the same email."
        )

    if await is_duplicate(db, User, User.username, dto.username):
        raise duplicate_error(
            target="username", msg="This username isn't available. Please try another."
        )

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

    return create_access_token(user.id)


@router.post("/verify-otp")
async def verify_otp(
    user_dep: user_dependency, db: db_dependency, dto: UserOtpVerifyDto
):
    user: User = await get_user_by_id(db, user_dep.get("id"))

    if user.email_otp != dto.email_otp:
        raise not_found_error("email-otp", "Invalid OTP")

    user.email_verified = True
    user.email_otp = None

    db.add(user)
    db.commit()
    db.refresh(user)

    return success_responce("OTP verification successful.")


@router.post("/login")
async def login(db: db_dependency, dto: UserLoginDto):
    user: User = await authenticate_user(
        db, username=dto.username, password=dto.password
    )
    return create_access_token(user.id)
