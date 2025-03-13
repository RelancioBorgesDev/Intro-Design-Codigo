from abc import ABC, abstractmethod
from typing import List


class DriverHandlerInterface(ABC):

    @classmethod
    @abstractmethod
    def standard_deviation(cls, number: List[float]) -> float:
        pass

    @classmethod
    @abstractmethod
    def variance(self, number: List[float]) -> float:
        pass

    @classmethod
    @abstractmethod
    def median_of_a_list(self, numbers: List[float]) -> float:
        pass