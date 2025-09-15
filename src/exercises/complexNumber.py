from __future__ import annotations

from math import cos, exp, sin, isclose

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
        self.real = a
        self.imaginary = b
        self.complex = a + b * 1j

    def __eq__(
        self,
        other: object,
    ) -> bool:
        if not isinstance(other, complexNumber):
            raise ValueError("Can only compare with another complexNumber instance.")

        return isclose(self.real, other.real) and isclose(self.imaginary, other.imaginary)

    def __repr__(self) -> str:
        return f"complexNumber({self.real}, {self.imaginary})"

    def conjugate(self) -> complexNumber:
        return complexNumber(self.real, -self.imaginary)

    def __abs__(self) -> float:
        return float((self.real**2 + self.imaginary**2) ** 0.5)

    def __absoluteSq__(self) -> float:
        return self.real**2 + self.imaginary**2

    def __add__(self, other: complexNumber) -> complexNumber:
        return complexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other: complexNumber) -> complexNumber:
        return complexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other: complexNumber) -> complexNumber:
        return complexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.imaginary * other.real + self.real * other.imaginary,
        )

    def __reciprocal__(self) -> complexNumber:
        denom = self.real**2 + self.imaginary**2
        return complexNumber(self.real / denom, -self.imaginary / denom)

    def __truediv__(self, other: complexNumber) -> complexNumber:
        return self.__mul__(other.__reciprocal__())

    def exp(self) -> complexNumber:
        exp_a = exp(self.real)
        return complexNumber(exp_a * cos(self.imaginary), exp_a * sin(self.imaginary))
