import datetime

from pydantic import BaseModel

from app.company.domain.aggregates import Company


class CompanyBase(BaseModel):
    name: str


class ReadCompanyDTO(CompanyBase):
    company_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    @staticmethod
    def from_entity(
        company: Company,
    ) -> "ReadCompanyDTO":
        return ReadCompanyDTO(**company.to_snapshot())


class CreateCompanyDTO(CompanyBase):
    pass


class UpdateCompanyDTO(CompanyBase):
    pass
