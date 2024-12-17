# pylint:disable=too-many-instance-attributes, too-many-positional-arguments
from datetime import datetime
from typing import Any

from app.employee.application.helpers import to_isoformat_or_none


class SeniorityLevel:
    def __init__(
        self,
        seniority_level_id: int | None = None,
        levelname: str | None = None,
        multiplier: float | None = None,
        time_needed: float | None = None,
        company_id: int | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ) -> None:
        self._seniority_level_id = seniority_level_id
        self._levelname = levelname
        self._multiplier = multiplier
        self._time_needed = time_needed
        self._company_id = company_id
        self._created_at = created_at
        self._updated_at = updated_at

    def to_snapshot(self) -> dict[str, Any]:
        created_at = to_isoformat_or_none(self._created_at)
        updated_at = to_isoformat_or_none(self._updated_at)
        return {
            "seniority_level_id": self._seniority_level_id,
            "levelname": self._levelname,
            "multiplier": self._multiplier,
            "time_needed": self._time_needed,
            "company_id": self._company_id,
            "created_at": created_at,
            "updated_at": updated_at,
        }

    def update(
        self,
        update_data: dict[str, Any],
    ) -> "SeniorityLevel":
        for key, value in update_data.items():
            if "key" in [
                "created_at",
                "updated_at",
                "seniority_level_id",
            ]:
                continue
            setattr(self, f"_{key}", value)
        return self

    @classmethod
    def create(
        cls,
        levelname: str,
        multiplier: float,
        time_needed: float,
        company_id: int,
    ) -> "SeniorityLevel":
        seniority_level = cls(
            seniority_level_id=None,
            levelname=levelname,
            multiplier=multiplier,
            time_needed=time_needed,
            company_id=company_id,
        )

        return seniority_level
