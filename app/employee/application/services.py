import logging

from app.company.infrastructure.repositories import CompanyRepository
from app.employee.application.dto import CreateEmployeeDTO, ReadEmployeeDTO
from app.employee.application.helpers import (
    find_correct_seniority_level_by_experience,
    generate_employee_email,
    generate_employee_experience,
)
from app.employee.domain.aggregates import Employee
from app.employee.infrastructure.repositories import EmployeeRepository
from app.seniority_level.infrastructure.repositories import (
    SeniorityLevelRepository,
)

logger = logging.getLogger(__name__)


class EmployeeFinder:
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    def find_by_id(self, id_: int) -> ReadEmployeeDTO:
        employee = self.repository.find_by_id(id_)
        return ReadEmployeeDTO.from_entity(employee)

    def findall(self) -> list[ReadEmployeeDTO]:
        employees = self.repository.findall()
        return [
            ReadEmployeeDTO.from_entity(employee) for employee in employees
        ]


class EmployeeCreator:
    def __init__(
        self,
        repository: EmployeeRepository,
        company_repository: CompanyRepository,
        seniority_levels_repository: SeniorityLevelRepository,
    ):
        self.repository = repository
        self.company_repository = company_repository
        self.seniority_levels_repository = seniority_levels_repository

    def create(
        self,
        create_employee: CreateEmployeeDTO,
    ) -> ReadEmployeeDTO:
        logger.info("Creating employee")
        company = self.company_repository.find_by_id(
            create_employee.company_id
        )
        seniority_levels = self.seniority_levels_repository.find_by_company_id(
            company._company_id
        )
        experience_time = generate_employee_experience(
            create_employee.jobstartdate, create_employee.experience
        )
        seniority_based_by_employee = (
            find_correct_seniority_level_by_experience(
                experience_time, seniority_levels
            )
        )
        if not seniority_levels:
            raise ValueError("Seniority Level is not compatible.")
        email = generate_employee_email(
            create_employee.name, create_employee.lastname, company._name
        )
        employee_data = create_employee.model_dump(exclude_unset=True)
        employee_data = Employee.create(
            **employee_data,
            email=email,
            senioritylevel_id=seniority_based_by_employee._seniority_level_id,
        )
        self.repository.save(employee_data)
        return ReadEmployeeDTO.from_entity(employee_data)
