from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from typing import Annotated
from utils.moment import get_moment_by_id
from utils.files import upload_file
from models.cherish_relation import CherishRelation
from utils.errors import conflit_error, not_found_error
from models.moment import Moment
from utils.helpers import get_db, success_responce, text_sentiment
from schemas.moment import MomentCreateDto
from core.security import get_current_user


router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.post("/")
async def create_moment(
    user_dep: user_dependency, db: db_dependency, dto: MomentCreateDto
):
    if not dto.message and not dto.photo:
        raise conflit_error(
            "moment",
            "Atleast a text or photo is necessary when posting a moment.",
        )

    if dto.message:
        senti = await text_sentiment(dto.message)
        if senti.get("Sentiment") == "NEGATIVE":
            raise conflit_error(
                "message",
                "Your message holds an negative tone. Please spread positivity.",
            )

    photo = None
    if dto.photo:
        file = await upload_file(dto.photo)
        photo = file.get("url")

    private = False
    if dto.private != None:
        private = dto.private

    moment = Moment(
        message=dto.message, photo=photo, private=private, user_id=user_dep.get("id")
    )

    db.add(moment)
    db.commit()
    db.refresh(moment)

    return moment


@router.delete("/{moment_id}")
async def delete_moment(
    user_dep: user_dependency,
    db: db_dependency,
    moment_id: str = Path(min_length=36, max_length=36),
):
    moment = (
        db.query(Moment)
        .filter(Moment.user_id == user_dep.get("id"))
        .filter(Moment.id == moment_id)
        .first()
    )

    if not moment:
        raise not_found_error(
            "moment",
            f"There exist no moment with the id {moment_id}",
        )

    db.delete(moment)
    db.commit()

    return success_responce()


@router.post("/cherish/{moment_id}")
async def cherish_moment(
    user_dep: user_dependency,
    db: db_dependency,
    moment_id: str = Path(min_length=36, max_length=36),
):
    moment = await get_moment_by_id(db, moment_id)

    if not moment:
        raise not_found_error(
            "moment", f"There exist no moment with the id {moment_id}"
        )

    cherished = (
        db.query(CherishRelation)
        .filter(CherishRelation.user_id == user_dep.get("id"))
        .filter(CherishRelation.moment_id == moment_id)
        .first()
    )

    if cherished:
        raise conflit_error("cherish", "You have already cherished this moment")

    cherish = CherishRelation(user_id=user_dep.get("id"), moment_id=moment_id)
    moment.total_cherishes += 1

    db.add(moment)
    db.add(cherish)
    db.commit()
    db.refresh(cherish)
    db.refresh(moment)

    return success_responce()


@router.get("/feed")
async def get_user_moments(user_dep: user_dependency, db: db_dependency):
    moments = (
        db.query(Moment)
        .filter(Moment.user_id != user_dep.get("id"))
        .filter(Moment.private == False)
        .all()
    )

    return moments
