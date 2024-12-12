import logging

from app.company.application.dto import CreateCompanyDTO, ReadCompanyDTO
from app.company.domain.aggregates import Company
from app.company.infrastructure.repositories import CompanyRepository

logger = logging.getLogger(__name__)


class CompanyFinder:
    def __init__(self, repository: CompanyRepository):
        self.repository = repository

    def find_by_id(self, id_: int) -> ReadCompanyDTO:
        company = self.repository.find_by_id(id_)
        return ReadCompanyDTO.from_entity(company)

    def findall(self) -> list[ReadCompanyDTO]:
        companies = self.repository.findall()
        return [ReadCompanyDTO.from_entity(company) for company in companies]


class CompanyCreator:
    def __init__(
        self,
        repository: CompanyRepository,
    ):
        self.repository = repository

    def create(
        self,
        create_company: CreateCompanyDTO,
    ) -> ReadCompanyDTO:
        logger.info("Creating company")
        company_data = create_company.model_dump(exclude_unset=True)
        company_data = Company.create(**company_data)
        self.repository.save(company_data)
        return ReadCompanyDTO.from_entity(company_data)
