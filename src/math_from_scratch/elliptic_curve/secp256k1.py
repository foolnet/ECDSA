from src.math_from_scratch.curve_point import CurvePoint
from src.math_from_scratch.elliptic_curve.abstract_curve import Curve


class Secp256k1(Curve):
    """Implementation of the secp256k1 elliptic curve."""

    def __init__(self):
        self._field_prime = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
        gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
        gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
        self._generator = CurvePoint(self, (gx, gy))

    @property
    def name(self) -> str:
        return "secp256k1"

    @property
    def a(self) -> int:
        return 0

    @property
    def b(self) -> int:
        return 7

    @property
    def field_prime(self) -> int:
        return self._field_prime

    @property
    def generator(self) -> CurvePoint:
        return self._generator

    @property
    def order(self) -> int:
        return 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
