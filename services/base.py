from abc import ABC, abstractmethod
from typing import Optional

from pydantic import BaseModel
from typing_extensions import Generic, TypeVar

from core import LoggerConfig

T = TypeVar("T")
U = TypeVar("U")


class BaseService(ABC, Generic[T, U]):
    def __init__(self):
        self._logger = LoggerConfig.get_logger(name=self.__class__.__name__)

    @abstractmethod
    def _convert_to_dto(self, model: T) -> U:
        """
        Convert SQLAlchemy model to DTO object
        :param model: SQLAlchemy model
        :return: DTO object
        """
        raise NotImplementedError



class ServiceResult(BaseModel, Generic[T]):
    is_success: bool
    data: Optional[T] = None
    error: Optional[str] = None

    @classmethod
    def success(cls, data: T):
        return cls(is_success=True, data=data)

    @classmethod
    def failure(cls, error: str):
        return cls(is_success=False, error=error)
