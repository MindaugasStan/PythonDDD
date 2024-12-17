import datetime

from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.company.infrastructure.db_models import Company
from app.core.base_db_model import BasePlusDateTime
from app.seniority_level.infrastructure.db_models import SeniorityLevel


class Employee(BasePlusDateTime):
    __tablename__ = "employees"

    employee_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    lastname: Mapped[str] = mapped_column(Text, nullable=False)
    email: Mapped[str] = mapped_column(Text, nullable=False)
    jobstartdate: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
    )
    jobenddate: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    hourlyrate: Mapped[float] = mapped_column()
    experience: Mapped[float] = mapped_column()

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.company_id", ondelete="CASCADE"),
    )
    employee_company: Mapped["Company"] = relationship(
        "Company",
        back_populates="employees",
        lazy="joined",
    )

    senioritylevel_id: Mapped[int] = mapped_column(
        ForeignKey("seniority_levels.seniority_level_id", ondelete="CASCADE"),
    )
    seniority_level: Mapped["SeniorityLevel"] = relationship(
        "SeniorityLevel",
        back_populates="employees",
        lazy="joined",
    )
