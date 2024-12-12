from datetime import datetime

from dateutil.relativedelta import relativedelta


def generate_employee_email(name, lastname, company):
    email = name + "." + lastname + "@" + company + ".com"
    email = email.replace(" ", "_").lower()
    return email


def generate_employee_experience(startdate, experience):
    now1 = datetime.now()
    now = datetime.date(now1)
    rdelta = relativedelta(now, startdate)
    time = float(rdelta.years) + experience
    return time


def to_isoformat_or_none(value: datetime | None) -> str | None:
    return value.astimezone().isoformat() if value else None


def from_isoformat_or_none(value: str | None) -> datetime | None:
    return datetime.fromisoformat(value) if value else None
