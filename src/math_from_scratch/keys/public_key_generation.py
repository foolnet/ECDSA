from src.math_from_scratch.curve_point import CurvePoint
from src.math_from_scratch.elliptic_curve.secp256k1 import Secp256k1


def generate_public_key(private_key) -> CurvePoint:
    generator_point = Secp256k1().generator
    return generator_point.multiply(private_key)
