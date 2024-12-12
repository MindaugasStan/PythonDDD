from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.seniority_level.application.services import (
    SeniorityLevelCreator,
    SeniorityLevelFinder,
)
from app.seniority_level.infrastructure.repositories import (
    SeniorityLevelRepository,
)


def seniority_level_repository(
    session: Session = Depends(get_db),
) -> SeniorityLevelRepository:
    return SeniorityLevelRepository(session)


def seniority_level_finder(
    repository: SeniorityLevelRepository = Depends(seniority_level_repository),
) -> SeniorityLevelFinder:
    return SeniorityLevelFinder(repository)


def seniority_level_creator(
    repository: SeniorityLevelRepository = Depends(seniority_level_repository),
) -> SeniorityLevelCreator:
    return SeniorityLevelCreator(repository)
