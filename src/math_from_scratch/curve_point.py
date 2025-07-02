from typing import Optional, Tuple


class CurvePoint:
    def __init__(self, curve: 'Curve', point: Optional[Tuple[int, int]]):
        self.curve = curve
        self.point = point

        if point is not None:
            x, y = point
            p = curve.field_prime
            x = x % p
            y = y % p
            self.point = (x, y)

            left = (y * y) % p
            right = (x ** 3 + curve.a * x + curve.b) % p
            if left != right:
                raise ValueError(f"Point {point} is not on the curve")

    def add(self, other: 'CurvePoint') -> 'CurvePoint':
        """Add two points on the elliptic curve."""
        if self.curve != other.curve:
            raise ValueError("Points must be on the same curve")

        p = self.curve.field_prime
        point1 = self.point
        point2 = other.point

        if point1 is None:
            return CurvePoint(self.curve, point2)
        if point2 is None:
            return CurvePoint(self.curve, point1)

        x1, y1 = point1
        x2, y2 = point2
        if (x1 == x2) and (y1 + y2) % p == 0:
            return CurvePoint(self.curve, None)

        if (x1 == x2) and (y2 == y1):
            nom = (3 * x1 ** 2 + self.curve.a) % p
            den = (2 * y1) % p
            den_inv = pow(den, p - 2, p)  # Fermat's little theorem
            s = (nom * den_inv) % p
        else:
            s = (((y2 - y1) % p) * pow(x2 - x1, p - 2, p)) % p

        x3 = (s ** 2 - x1 - x2) % p
        y3 = (s * (x1 - x3) - y1) % p

        return CurvePoint(self.curve, (x3, y3))

    def multiply(self, n: int) -> 'CurvePoint':
        """Scalar multiplication using double-and-add algorithm."""
        if not isinstance(n, int):
            raise TypeError("Scalar must be an integer")

        if n == 0:
            return CurvePoint(self.curve, None)

        if n < 0:
            if self.point is None:
                return CurvePoint(self.curve, None)
            x, y = self.point
            p = self.curve.field_prime
            neg_point = (x, (-y) % p)
            return CurvePoint(self.curve, neg_point).multiply(-n)

        result = CurvePoint(self.curve, None)
        addend = self
        while n:
            if n & 1:
                result = result.add(addend)
            addend = addend.add(addend)
            n >>= 1

        return result

    def __repr__(self) -> str:
        if self.point is None:
            return f"CurvePoint(∞)"
        x, y = self.point
        return f"CurvePoint({hex(x)}, {hex(y)})"

    def __eq__(self, other: 'CurvePoint') -> bool:
        if not isinstance(other, CurvePoint):
            return False
        return self.point == other.point and self.curve == other.curve
