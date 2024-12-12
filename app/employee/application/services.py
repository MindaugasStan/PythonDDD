import logging

from app.employee.application.dto import CreateEmployeeDTO, ReadEmployeeDTO
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
    ):
        self.repository = repository

    def create(
        self,
        create_employee: CreateEmployeeDTO,
    ) -> ReadEmployeeDTO:
        logger.info("Creating employee")
        employee_data = create_employee.model_dump(exclude_unset=True)
        employee_data = Employee.create(**employee_data)
        self.repository.save(employee_data)
        return ReadEmployeeDTO.from_entity(employee_data)
