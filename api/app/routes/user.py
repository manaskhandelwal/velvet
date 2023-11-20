from typing import Annotated
from models.moment import Moment
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import UserUpdateProfileDto
from utils.files import upload_file
from utils.errors import conflit_error
from models.follow_relation import FollowRelation
from models.user import User
from utils.user import get_user_by_id, get_user_by_username
from utils.helpers import get_db, success_responce
from core.security import get_current_user


router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.get("/p/{username}")
async def get_user_profile(db: db_dependency, username: str):
    user: User = await get_user_by_username(db, username)

    profile = user.__dict__

    profile.pop("id")
    profile.pop("hashed_password")
    profile.pop("email")
    profile.pop("email_otp")
    profile.pop("email_verified")

    return profile


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


@router.post("/follow/{to_follow_user_id}")
async def follow_user(
    user_dep: user_dependency, db: db_dependency, to_follow_user_id: str
):
    followed = (
        db.query(FollowRelation)
        .filter(FollowRelation.user_id == user_dep.get("id"))
        .filter(FollowRelation.followed_user_id == to_follow_user_id)
        .first()
    )

    if followed:
        raise conflit_error("follow", f"You are already following this account.")

    follow = FollowRelation(
        user_id=user_dep.get("id"), followed_user_id=to_follow_user_id
    )

    user: User = await get_user_by_id(db, user_dep.get("id"))
    to_follow_user: User = await get_user_by_id(db, to_follow_user_id)

    user.total_following += 1
    to_follow_user.total_followers += 1

    db.add(follow)
    db.add(user)
    db.add(to_follow_user)

    db.commit()

    db.refresh(follow)
    db.refresh(user)
    db.refresh(to_follow_user)

    return success_responce()


@router.post("/unfollow/{to_unfollow_user_id}")
async def unfollow_user(
    user_dep: user_dependency, db: db_dependency, to_unfollow_user_id: str
):
    unfollowed = (
        db.query(FollowRelation)
        .filter(FollowRelation.user_id == user_dep.get("id"))
        .filter(FollowRelation.followed_user_id == to_unfollow_user_id)
        .first()
    )

    if not unfollowed:
        raise conflit_error("follow", f"You are anyways not following this account.")

    follow = FollowRelation(
        user_id=user_dep.get("id"), followed_user_id=to_unfollow_user_id
    )

    user: User = await get_user_by_id(db, user_dep.get("id"))
    to_follow_user: User = await get_user_by_id(db, to_unfollow_user_id)

    user.total_following -= 1
    to_follow_user.total_followers -= 1

    db.add(follow)
    db.add(user)
    db.add(to_follow_user)

    db.commit()

    db.refresh(follow)
    db.refresh(user)
    db.refresh(to_follow_user)

    return success_responce()


@router.post("/update-profile")
async def update_profile(
    user_dep: user_dependency, db: db_dependency, dto: UserUpdateProfileDto
):
    user: User = await get_user_by_id(db, user_dep.get("id"))

    photo = await upload_file(dto.profile_photo)

    user.profile_photo = photo.get("url")
    user.pronouns = dto.pronouns
    user.bio = dto.bio
    user.private = dto.private

    db.add(user)
    db.commit()
    db.refresh(user)

    return success_responce()


@router.get("/moments")
async def get_user_moments(user_dep: user_dependency, db: db_dependency):
    moments = db.query(Moment).filter(Moment.user_id == user_dep.get("id")).all()

    return moments
