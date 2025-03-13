from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import (
    DriverHandlerInterface
)


class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        median = self.__calculate_median(input_data)
        formated_response = self.__format_response(median)

        return formated_response

    def calculate_mean(self, request: FlaskRequest) -> Dict:  # Nova função para calcular a média
        body = request.json
        input_data = self.__validate_body(body)

        mean = self.__calculate_mean(input_data)
        formated_response = self.__format_response(mean, operation="Mean")

        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado!")

        input_data = body["numbers"]
        return input_data

    def __calculate_median(self, numbers: List[float]) -> float:
        median = self.__driver_handler.median_of_a_list(numbers)
        return median

    def __calculate_mean(self, numbers: List[float]) -> float:  # Novo cálculo de média
        return sum(numbers) / len(numbers) if numbers else 0

    def __format_response(self, value: float, operation="Median") -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "Operation": operation,
                "value": value,
                "Success": True,
            }
        }
