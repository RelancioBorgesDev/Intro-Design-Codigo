from .calculator_4 import Calculator4
from typing import Dict, List


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def median_of_a_list(number: List[float]) -> float:
    return 3


class MockDriverHandler:
    pass


def test_calculate_mean():
    mock_request = MockRequest({"numbers": [10, 20, 30, 40, 50]})
    calculator_4 = Calculator4(MockDriverHandler())

    response = calculator_4.calculate_mean(mock_request)

    assert response == {
        "data": {
            "Calculator": 4,
            "Operation": "Mean",
            "value": 30.0,
            "Success": True,
        }
    }
