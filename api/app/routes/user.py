from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.user import User
from utils.user import get_user_by_id
from utils.helpers import get_db
from core.security import get_current_user


router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/me")
async def get_user_profile(user_dep: user_dependency, db: db_dependency):
    user: User = await get_user_by_id(db, user_dep.get("id"))
    profile = user.__dict__

    profile.pop("id")
    profile.pop("hashed_password")
    profile.pop("email")
    profile.pop("email_otp")
    profile.pop("email_verified")

    return profile
