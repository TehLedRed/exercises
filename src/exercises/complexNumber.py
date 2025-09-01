from __future__ import annotations

from math import cos, exp, sin

NUMBER = int | float


class complexNumber(object):
    """
    A complex number is expressed in the form z = a + b * i, where:
    a is the real part (a real number),
    b is the imaginary part (also a real number), and
    i is the imaginary unit satisfying i^2 = -1.
    """

    def __init__(
        self,
        a: NUMBER,
        b: NUMBER,
    ) -> None:
        self.a = a
        self.b = b
        self.complex = a + b * 1j

    def __conjugate__(self) -> complexNumber:
        return complexNumber(self.a, -self.b)

    def __abs__(self) -> float:
        return float((self.a**2 + self.b**2) ** 0.5)

    def __absoluteSq__(self) -> float:
        return self.a**2 + self.b**2

    def __add__(self, other: complexNumber) -> complexNumber:
        return complexNumber(self.a + other.a, self.b + other.b)

    def __sub__(self, other: complexNumber) -> complexNumber:
        return complexNumber(self.a - other.a, self.b - other.b)

    def __mul__(self, other: complexNumber) -> complexNumber:
        return complexNumber(
            self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b
        )

    def __reciprocal__(self) -> complexNumber:
        denom = self.a**2 + self.b**2
        return complexNumber(self.a / denom, -self.b / denom)

    def __div__(self, other: complexNumber) -> complexNumber:
        return self.__mul__(other.__reciprocal__())

    def __exponentiation__(self) -> complexNumber:
        exp_a = exp(self.a)
        return complexNumber(exp_a * cos(self.b), exp_a * sin(self.b))
