from datetime import datetime

from dateutil.relativedelta import relativedelta


def generate_employee_email(name: str, lastname: str, company: str) -> str:
    email = name + "." + lastname + "@" + company + ".com"
    email = email.replace(" ", "_").lower()
    return email


def generate_employee_experience(
    startdate: datetime, experience: float
) -> float:
    now = datetime.now(startdate.tzinfo)
    rdelta = relativedelta(now, startdate)
    time = float(rdelta.years) + experience
    return time


def find_correct_seniority_level_by_experience(experience, seniority_levels):
    correct_level = None
    for level in seniority_levels:
        if experience >= level._time_needed:
            if (
                correct_level is None
                or level._time_needed > correct_level._time_needed
            ):
                correct_level = level
    return correct_level


def to_isoformat_or_none(value: datetime | None) -> str | None:
    return value.astimezone().isoformat() if value else None


def from_isoformat_or_none(value: str | None) -> datetime | None:
    return datetime.fromisoformat(value) if value else None
