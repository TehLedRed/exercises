from __future__ import annotations

from math import gcd
from typing import Any


class rationalNumber(object):
    """
    A rational number is defined as the quotient of two integers a and b,
    called the numerator and denominator, respectively, where b != 0.
    source: https://exercism.org/exercises/rational-numbers

    Args:
        object (_type_): _description_
    """

    def __init__(
        self,
        a: int,
        b: int,
    ) -> None:
        if not b:
            raise ValueError("Denominator can't be zero.")

        numFactor = gcd(a, b)
        self.numerator = int(a / numFactor)
        self.denominator = int(b / numFactor)

        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, rationalNumber):
            return False
        return (
            self.numerator == other.numerator and self.denominator == other.denominator
        )

    def __repr__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def __abs__(self) -> rationalNumber:
        return rationalNumber(abs(self.numerator), abs(self.denominator))

    def __add__(self, other: rationalNumber) -> rationalNumber:
        new_numerator = (self.numerator * other.denominator) + (
            other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator

        return rationalNumber(new_numerator, new_denominator)

    def __sub__(self, other: rationalNumber) -> rationalNumber:
        new_numerator = (self.numerator * other.denominator) - (
            other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator

        return rationalNumber(new_numerator, new_denominator)

    def __mul__(self, other: rationalNumber) -> rationalNumber:
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return rationalNumber(new_numerator, new_denominator)

    def __truediv__(self, other: rationalNumber) -> rationalNumber:
        if other.numerator == 0:
            raise ValueError("Numerator of incoming rational number can't be zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator

        return rationalNumber(new_numerator, new_denominator)

    def __pow__(self, power: int) -> rationalNumber | float:
        """
        Exponentiation of a rational number r = a/b to a non-negative integer
        power n is r^n = (a^n)/(b^n).

        Exponentiation of a rational number r = a/b to a negative integer power
        n is r^n = (b^m)/(a^m), where m = |n|.

        Args:
            power (int): _description_

        Returns:
            rationalNumber: _description_
        """
        if power < 0:
            new_numerator = self.denominator ** abs(power)
            new_denominator = self.numerator ** abs(power)
        else:
            new_numerator = self.numerator**power
            new_denominator = self.denominator**power

        return rationalNumber(new_numerator, new_denominator)

    def __rpow__(self, power: float) -> float:
        return float(self.numerator**power) / float(self.denominator**power)
