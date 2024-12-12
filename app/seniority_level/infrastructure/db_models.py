from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.base_db_model import BasePlusDateTime


class SeniorityLevel(BasePlusDateTime):
    __tablename__ = "seniority_levels"
    seniority_level_id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    levelname: Mapped[str] = mapped_column(Text, nullable=False)
    multiplier: Mapped[float] = mapped_column()
    time_needed: Mapped[float] = mapped_column()
    company_id: Mapped[int] = mapped_column(
        ForeignKey(
            "companies.company_id",
            ondelete="RESTRICT",
        ),
    )
    company: Mapped["Company"] = relationship(
        lazy="joined", cascade="all, delete-orphan"
    )