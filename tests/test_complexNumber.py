from math import e, log, pi
from typing import TypedDict
from typing_extensions import Unpack

from pytest import approx
from exercises.complexNumber import complexNumber


class ApproxKwargs(TypedDict, total=False):
    rel: float
    abs: float
    nan_ok: bool


def complexNumber_approx(c1: complexNumber, c2: complexNumber, **kwargs: Unpack[ApproxKwargs]) -> bool:
    return approx(c1.real, **kwargs) == approx(c2.real, **kwargs) and approx(
        c1.imaginary, **kwargs
    ) == approx(c2.imaginary, **kwargs)


def test_real_part_of_a_purely_real_number() -> None:
    assert 1 == complexNumber(1, 0).real


def test_real_part_of_a_purely_imaginary_number() -> None:
    assert 0 == complexNumber(0, 1).real


def test_real_part_of_a_number_with_real_and_imaginary_part() -> None:
    assert 1 == complexNumber(1, 2).real


# Imaginary part


def test_imaginary_part_of_a_purely_real_number() -> None:
    assert 0 == complexNumber(1, 0).imaginary


def test_imaginary_part_of_a_purely_imaginary_number() -> None:
    assert 1 == complexNumber(0, 1).imaginary


def test_imaginary_part_of_a_number_with_real_and_imaginary_part() -> None:
    assert 2 == complexNumber(1, 2).imaginary


# Equality


def test_equality_first() -> None:
    assert complexNumber(1, 0) == complexNumber(1, 0)


def test_equality_second() -> None:
    assert complexNumber(1, 0) != complexNumber(2, 0)


# Arithmetic

# Addition


def test_add_purely_real_numbers() -> None:
    assert complexNumber(1, 0) + complexNumber(2, 0) == complexNumber(3, 0)


def test_add_purely_imaginary_numbers() -> None:
    assert complexNumber(0, 1) + complexNumber(0, 2) == complexNumber(0, 3)


def test_add_numbers_with_real_and_imaginary_part() -> None:
    assert complexNumber(1, 2) + complexNumber(3, 4) == complexNumber(4, 6)


# Subtraction


def test_subtract_purely_real_numbers() -> None:
    assert complexNumber(1, 0) - complexNumber(2, 0) == complexNumber(-1, 0)


def test_subtract_purely_imaginary_numbers() -> None:
    assert complexNumber(0, 1) - complexNumber(0, 2) == complexNumber(0, -1)


def test_subtract_numbers_with_real_and_imaginary_part() -> None:
    assert complexNumber(1, 2) - complexNumber(3, 4) == complexNumber(-2, -2)


# Multiplication


def test_imaginary_unit() -> None:
    assert complexNumber(0, 1) * complexNumber(0, 1) == complexNumber(-1, 0)


def test_multiply_purely_real_numbers() -> None:
    assert complexNumber(1, 0) * complexNumber(2, 0) == complexNumber(2, 0)


def test_multiply_purely_imaginary_numbers() -> None:
    assert complexNumber(0, 1) * complexNumber(0, 2) == complexNumber(-2, 0)


def test_multiply_numbers_with_real_and_imaginary_part() -> None:
    assert complexNumber(1, 2) * complexNumber(3, 4) == complexNumber(-5, 10)


# Division


def test_divide_purely_real_numbers() -> None:
    assert complexNumber(1, 0) / complexNumber(2, 0) == complexNumber(0.5, 0)


def test_divide_purely_imaginary_numbers() -> None:
    assert complexNumber(0, 1) / complexNumber(0, 2) == complexNumber(0.5, 0)


def test_divide_numbers_with_real_and_imaginary_part() -> None:
    assert complexNumber(1, 2) / complexNumber(3, 4) == complexNumber(0.44, 0.08)


# Absolute value


def test_absolute_value_of_a_positive_purely_real_number() -> None:
    assert abs(complexNumber(5, 0)) == 5


def test_absolute_value_of_a_negative_purely_real_number() -> None:
    assert abs(complexNumber(-5, 0)) == 5


def test_absolute_value_of_a_purely_imaginary_number_with_positive_imaginary_part() -> (
    None
):
    assert abs(complexNumber(0, 5)) == 5


def test_absolute_value_of_a_purely_imaginary_number_with_negative_imaginary_part() -> (
    None
):
    assert abs(complexNumber(0, -5)) == 5


def test_absolute_value_of_a_number_with_real_and_imaginary_part() -> None:
    assert abs(complexNumber(3, 4)) == 5


# complexNumber conjugate


def test_conjugate_a_purely_real_number() -> None:
    assert complexNumber(5, 0).conjugate() == complexNumber(5, 0)


def test_conjugate_a_purely_imaginary_number() -> None:
    assert complexNumber(0, 5).conjugate() == complexNumber(0, -5)


def test_conjugate_a_number_with_real_and_imaginary_part() -> None:
    assert complexNumber(1, 1).conjugate() == complexNumber(1, -1)


# complexNumber exponential function


def test_exponential_of_0() -> None:
    assert complexNumber(0, 0).exp() == complexNumber(1, 0)


def test_euler_s_identity_formula() -> None:
    assert complexNumber_approx(complexNumber(0, pi).exp(), complexNumber(-1, 0), abs=0.01)


def test_exponential_of_a_purely_real_number() -> None:
    assert complexNumber_approx(complexNumber(1, 0).exp(), complexNumber(e, 0), abs=0.01)


def test_exponential_of_a_number_with_real_and_imaginary_part() -> None:
    assert complexNumber_approx(complexNumber(log(2), pi).exp(), complexNumber(-2, 0), abs=0.01)


def test_exponential_resulting_in_a_number_with_real_and_imaginary_part() -> None:
    assert complexNumber_approx(complexNumber(log(2) / 2, pi / 4).exp(), complexNumber(1, 1), abs=0.01)


# Additional tests for this track


def test_equality_of_complexNumber_numbers() -> None:
    assert complexNumber(1, 2) == complexNumber(1, 2)


def test_inequality_of_real_part() -> None:
    assert complexNumber(1, 2) != complexNumber(2, 2)


def test_inequality_of_imaginary_part() -> None:
    assert complexNumber(1, 2) != complexNumber(1, 1)