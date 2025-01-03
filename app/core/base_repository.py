from abc import ABC, abstractmethod
from typing import Generic, Sequence, TypeVar

_T = TypeVar("_T")
_D = TypeVar("_D")


class BaseRepository(ABC, Generic[_T]):
    """
    Abstract generic Repository
    """

    @abstractmethod
    def create(self, agg: _D, entity: _T) -> _T:
        raise NotImplementedError()

    @abstractmethod
    def findall(self) -> Sequence[_T]:
        raise NotImplementedError()

    @abstractmethod
    def find_by_id(self, id_: int) -> _T | None:
        raise NotImplementedError()

    @abstractmethod
    def update(self, agg: _D, entity: _T) -> _T:
        raise NotImplementedError()

    @abstractmethod
    def delete_by_id(self, id_: int) -> _T:
        raise NotImplementedError()
