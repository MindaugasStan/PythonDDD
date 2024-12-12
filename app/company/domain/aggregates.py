# pylint:disable=too-many-instance-attributes, too-many-positional-arguments
from datetime import datetime
from typing import Any

from app.employee.application.helpers import to_isoformat_or_none


class Company:
    def __init__(
        self,
        company_id: int | None = None,
        name: str | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ) -> None:
        self._company_id = company_id
        self._name = name
        self._created_at = created_at
        self._updated_at = updated_at

    def to_snapshot(self) -> dict[str, Any]:
        created_at = to_isoformat_or_none(self._created_at)
        updated_at = to_isoformat_or_none(self._updated_at)
        return {
            "company_id": self._company_id,
            "name": self._name,
            "created_at": created_at,
            "updated_at": updated_at,
        }

    def update(
        self,
        update_data: dict[str, Any],
    ) -> "Company":
        for key, value in update_data.items():
            if "key" in [
                "created_at",
                "updated_at",
                "company_id",
            ]:
                continue
            setattr(self, f"_{key}", value)
        return self

    @classmethod
    def create(cls, name: str) -> "Company":
        company = cls(company_id=None, name=name)

        return company
