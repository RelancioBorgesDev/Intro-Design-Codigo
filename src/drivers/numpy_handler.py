import numpy
from typing import List, Any

from numpy import floating


class NumpyHandler:
    def __init__(self) -> None:
        self.__np = numpy

    def standard_deviation(self, numbers: List[float]) -> floating[Any]:
        return self.__np.std(numbers)

    def standard_deviation_with_param(self, numbers: List[float]) -> float:
        return self.__np.std(numbers, axis=[])

    def variance(self, numbers: List[float]) -> floating[Any]:
        return self.__np.var(numbers)

    def median_of_a_list(self, numbers: List[float]) -> floating[Any]:
        return self.__np.median(numbers)