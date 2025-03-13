from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import (
    DriverHandlerInterface
)
from src.errors.calculation_error import CalculationError
from src.errors.invalid_request_body import InvalidRequestBodyError


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
            raise InvalidRequestBodyError("O corpo da requisição deve conter a chave 'numbers'.")

        input_data = body["numbers"]
        if not isinstance(input_data, list) or not all(isinstance(n, (int, float)) for n in input_data):
            raise InvalidRequestBodyError("A chave 'numbers' deve ser uma lista de números.")

        if not input_data:
            raise CalculationError("A lista de números não pode estar vazia.")

        return input_data

