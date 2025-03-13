from flask import Blueprint, jsonify, request

from src.main.factories.calculator2_factory import calculator2_factory
from src.main.factories.calculator3_factory import calculator3_factory
from src.main.factories.calculator4_factory import calculator4_factory

calc_route_bp = Blueprint("calc_routes", __name__)


@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator1():
    print(request)
    return jsonify({
        "success": True,
        }), 200

@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator2():
    calc = calculator2_factory()
    response = calc.calculate(request)

    return jsonify(response), 200


@calc_route_bp.route("/calculator/3", methods=["POST"])
def calculator_3():
    calc = calculator3_factory()
    response = calc.calculate(request)

    return jsonify(response), 200

@calc_route_bp.route("/calculator/4", methods=["POST"])
def calculator_4():
    calc = calculator4_factory()
    response = calc.calculate(request)

    return jsonify(response), 200