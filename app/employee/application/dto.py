import datetime

from pydantic import BaseModel

from app.employee.domain.aggregates import Employee


class EmployeeBase(BaseModel):
    name: str
    lastname: str
    jobstartdate: datetime.datetime
    jobenddate: datetime.datetime | None = None
    experience: float
    hourlyrate: float
    company_id: int


class ReadEmployeeDTO(EmployeeBase):
    created_at: datetime.datetime
    updated_at: datetime.datetime

    @staticmethod
    def from_entity(
        employee: Employee,
    ) -> "ReadEmployeeDTO":
        return ReadEmployeeDTO(**employee.to_snapshot())


class CreateEmployeeDTO(EmployeeBase):
    pass


class UpdateEmployeeDTO(EmployeeBase):
    pass
