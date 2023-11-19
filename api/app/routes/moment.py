from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated
from models.cherish_relation import CherishRelation
from utils.errors import conflit_error
from models.moment import Moment
from utils.helpers import get_db, success_responce
from schemas.moment import MomentCherishDto, MomentCreateDto
from core.security import get_current_user


router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.post("/")
async def create_moment(
    user_dep: user_dependency, db: db_dependency, dto: MomentCreateDto
):
    # FIX: Use NLP to check for negative content

    moment = Moment(message=dto.message, user_id=user_dep.get("id"))

    db.add(moment)
    db.commit()
    db.refresh(moment)

    return success_responce()


@router.post("/cherish")
async def cherish_moment(
    user_dep: user_dependency, db: db_dependency, dto: MomentCherishDto
):
    cherished = (
        db.query(CherishRelation)
        .filter(CherishRelation.user_id == user_dep.get("id"))
        .filter(CherishRelation.moment_id == dto.moment_id)
        .first()
    )

    if cherished:
        raise conflit_error("cherish", "You have already cherished this moment")

    cherish = CherishRelation(user_id=user_dep.get("id"), moment_id=dto.moment_id)

    db.add(cherish)
    db.commit()
    db.refresh(cherish)

    return success_responce()
