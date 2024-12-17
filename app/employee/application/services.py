import logging

from app.company.infrastructure.repositories import CompanyRepository
from app.employee.application.dto import CreateEmployeeDTO, ReadEmployeeDTO
from app.employee.application.helpers import generate_employee_email
from app.employee.domain.aggregates import Employee
from app.employee.infrastructure.repositories import EmployeeRepository

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
    ):
        self.repository = repository
        self.company_repository = company_repository

    def create(
        self,
        create_employee: CreateEmployeeDTO,
    ) -> ReadEmployeeDTO:
        logger.info("Creating employee")
        company = self.company_repository.find_by_id(
            create_employee.company_id
        )
        email = generate_employee_email(
            create_employee.name, create_employee.lastname, company._name
        )
        employee_data = create_employee.model_dump(exclude_unset=True)
        employee_data = Employee.create(**employee_data, email=email)
        self.repository.save(employee_data)
        return ReadEmployeeDTO.from_entity(employee_data)
