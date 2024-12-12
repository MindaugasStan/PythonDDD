# pylint:disable=too-many-instance-attributes, too-many-positional-arguments
from datetime import datetime
from typing import Any

from app.employee.application.helpers import to_isoformat_or_none


class Employee:
    def __init__(
        self,
        name: str,
        lastname: str,
        jobstart_date: datetime,
        hourly_rate: float,
        experience: float,
        company_id: int,
        employee_id: int | None = None,
        jobend_date: datetime | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ) -> None:
        self._employee_id = employee_id
        self._name = name
        self._lastname = lastname
        self._jobstart_date = jobstart_date
        self._jobend_date = jobend_date
        self._hourly_rate = hourly_rate
        self._experience = experience
        self._company_id = company_id
        self._created_at = created_at
        self._updated_at = updated_at

    def to_snapshot(self) -> dict[str, Any]:
        created_at = to_isoformat_or_none(self._created_at)
        updated_at = to_isoformat_or_none(self._updated_at)
        return {
            "employee_id": self._employee_id,
            "name": self._name,
            "lastname": self._lastname,
            "jobstart_date": self._jobstart_date,
            "jobend_date": self._jobend_date,
            "hourly_rate": self._hourly_rate,
            "experience": self._experience,
            "company_id": self._company_id,
            "created_at": created_at,
            "updated_at": updated_at,
        }

    @classmethod
    def create(
        cls,
        name: str,
        lastname: str,
        jobstart_date: datetime,
        hourly_rate: float,
        experience: float,
        company_id: int,
    ) -> "Employee":
        employee = cls(
            employee_id=None,
            name=name,
            lastname=lastname,
            jobstart_date=jobstart_date,
            hourly_rate=hourly_rate,
            experience=experience,
            company_id=company_id,
        )

        return employee
