from .calculator_1 import Calculator1
from pytest import raises
from typing import Dict


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator_1 = Calculator1()
    response = calculator_1.calculate(mock_request)

    assert "data" in response
    assert "data" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})  # Requisição mal formatada
    calculator_1 = Calculator1()  # Criar instância corretamente

    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request)  # Chamar na instância

    assert str(excinfo.value) == "body mal formatado!"
