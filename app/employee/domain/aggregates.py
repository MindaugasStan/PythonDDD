# pylint:disable=too-many-instance-attributes, too-many-positional-arguments
from datetime import datetime
from typing import Any

from app.employee.application.helpers import to_isoformat_or_none


class Employee:
    def __init__(
        self,
        name: str,
        lastname: str,
        jobstartdate: datetime,
        hourlyrate: float,
        experience: float,
        company_id: int,
        employee_id: int | None = None,
        jobenddate: datetime | None = None,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
        email: str | None = None,
    ) -> None:
        self._employee_id = employee_id
        self._name = name
        self._lastname = lastname
        self._jobstartdate = jobstartdate
        self._jobenddate = jobenddate
        self._hourlyrate = hourlyrate
        self._experience = experience
        self._company_id = company_id
        self._created_at = created_at
        self._updated_at = updated_at
        self._email = email

    def to_snapshot(self) -> dict[str, Any]:
        created_at = to_isoformat_or_none(self._created_at)
        updated_at = to_isoformat_or_none(self._updated_at)
        return {
            "employee_id": self._employee_id,
            "name": self._name,
            "lastname": self._lastname,
            "jobstartdate": self._jobstartdate,
            "jobenddate": self._jobenddate,
            "hourlyrate": self._hourlyrate,
            "experience": self._experience,
            "company_id": self._company_id,
            "created_at": created_at,
            "updated_at": updated_at,
            "email": self._email,
        }

    @classmethod
    def create(
        cls,
        name: str,
        lastname: str,
        jobstartdate: datetime,
        hourlyrate: float,
        experience: float,
        company_id: int,
        email: str,
        jobenddate: datetime | None = None,
    ) -> "Employee":
        employee = cls(
            employee_id=None,
            name=name,
            lastname=lastname,
            jobstartdate=jobstartdate,
            jobenddate=jobenddate,
            hourlyrate=hourlyrate,
            experience=experience,
            company_id=company_id,
            email=email,
        )

        return employee
