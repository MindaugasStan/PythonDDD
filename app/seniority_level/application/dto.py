import datetime

from pydantic import BaseModel

from app.seniority_level.domain.aggregates import SeniorityLevel


class SeniorityBase(BaseModel):
    levelname: str
    multiplier: float
    time_needed: float
    company_id: int


class ReadSeniorityLevelDTO(SeniorityBase):
    seniority_level_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    @staticmethod
    def from_entity(
        seniority_level: SeniorityLevel,
    ) -> "ReadSeniorityLevelDTO":
        return ReadSeniorityLevelDTO(**seniority_level.to_snapshot())


class CreateSeniorityLevelDTO(SeniorityBase):
    pass


class UpdateSeniorityLevelDTO(SeniorityBase):
    pass
