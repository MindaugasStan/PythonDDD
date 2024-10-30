from abc import abstractmethod

from app.core.base_repository import BaseRepository


class UserRepository(BaseRepository):
    """UserRepository defines a repositories interface for User entity"""

    @abstractmethod
    def find_by_email(self, email: str) -> str | None:
        raise NotImplementedError()