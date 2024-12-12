# pylint: disable=unused-argument
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.seniority_level.application.dto import (
    CreateSeniorityLevelDTO,
    ReadSeniorityLevelDTO,
)
from app.seniority_level.application.services import (
    SeniorityLevelCreator,
    SeniorityLevelFinder,
)
from app.seniority_level.dependencies import (
    seniority_level_creator,
    seniority_level_finder,
)

level_router = APIRouter(
    prefix="/seniority_levels",
    tags=["Seniority levels"],
)


@level_router.get(
    "/{key}",
    response_model=ReadSeniorityLevelDTO,
)
def get_level(
    key: int,
    service: SeniorityLevelFinder = Depends(seniority_level_finder),
):
    level = service.find_by_id(key)
    return level


@level_router.get("/", response_model=list[ReadSeniorityLevelDTO])
def get_levels(
    service: SeniorityLevelFinder = Depends(seniority_level_finder),
):
    levels = service.findall()
    return levels


@level_router.post(
    "/",
    response_model=ReadSeniorityLevelDTO,
    status_code=status.HTTP_201_CREATED,
)
def create_seniority_level(
    data: CreateSeniorityLevelDTO,
    service: SeniorityLevelCreator = Depends(seniority_level_creator),
    session: Session = Depends(get_db),
):
    level = service.create(create_level=data)

    session.commit()

    return level
