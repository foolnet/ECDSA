from abc import ABC, abstractmethod

from src.math_from_scratch.curve_point import CurvePoint


class Curve(ABC):
    """y^2 = x^3 + ax + b."""

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def a(self) -> int:
        pass

    @property
    @abstractmethod
    def b(self) -> int:
        pass

    @property
    @abstractmethod
    def field_prime(self) -> int:
        pass

    @property
    @abstractmethod
    def generator(self) -> CurvePoint:
        pass

    @property
    @abstractmethod
    def order(self) -> int:
        pass

    def __eq__(self, other: 'Curve') -> bool:
        if not isinstance(other, Curve):
            return False
        return (self.name == other.name and
                self.a == other.a and
                self.b == other.b and
                self.field_prime == other.field_prime)
