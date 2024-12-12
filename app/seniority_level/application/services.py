import logging

from app.seniority_level.application.dto import (
    CreateSeniorityLevelDTO,
    ReadSeniorityLevelDTO,
)
from app.seniority_level.domain.aggregates import SeniorityLevel
from app.seniority_level.infrastructure.repositories import (
    SeniorityLevelRepository,
)

logger = logging.getLogger(__name__)


class SeniorityLevelFinder:
    def __init__(self, repository: SeniorityLevelRepository):
        self.repository = repository

    def find_by_id(self, id_: int) -> ReadSeniorityLevelDTO:
        seniority_level = self.repository.find_by_id(id_)
        return ReadSeniorityLevelDTO.from_entity(seniority_level)

    def findall(self) -> list[ReadSeniorityLevelDTO]:
        levels = self.repository.findall()
        return [ReadSeniorityLevelDTO.from_entity(level) for level in levels]


class SeniorityLevelCreator:
    def __init__(
        self,
        repository: SeniorityLevelRepository,
    ):
        self.repository = repository

    def create(
        self,
        create_level: CreateSeniorityLevelDTO,
    ) -> ReadSeniorityLevelDTO:
        logger.info("Creating seniority level")
        seniority_level_data = create_level.model_dump(exclude_unset=True)
        seniority_level_data = SeniorityLevel.create(**seniority_level_data)
        self.repository.save(seniority_level_data)
        return ReadSeniorityLevelDTO.from_entity(seniority_level_data)
