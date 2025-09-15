from pytest import raises

from exercises.rationalNumber import rationalNumber


def test_rational_number_init() -> None:
    r = rationalNumber(1, 2)
    assert r.numerator == 1
    assert r.denominator == 2


def test_rational_number_init_simplify() -> None:
    r = rationalNumber(2, 4)
    assert r.numerator == 1
    assert r.denominator == 2


def test_rational_number_init_negative() -> None:
    r = rationalNumber(-1, 2)
    assert r.numerator == -1
    assert r.denominator == 2

    r = rationalNumber(1, -2)
    assert r.numerator == -1
    assert r.denominator == 2

    r = rationalNumber(-1, -2)
    assert r.numerator == 1
    assert r.denominator == 2


def test_rational_number_init_zero_denominator() -> None:
    with raises(ValueError, match="Denominator can't be zero."):
        rationalNumber(1, 0)


def test_rational_number_abs() -> None:
    r = rationalNumber(-1, -2)
    abs_r = r.__abs__()
    assert abs_r.numerator == 1
    assert abs_r.denominator == 2


def test_rational_number_add() -> None:
    r1 = rationalNumber(1, 2)
    r2 = rationalNumber(1, 3)
    r3 = r1.__add__(r2)
    assert r3.numerator == 5
    assert r3.denominator == 6


def test_rational_number_sub() -> None:
    r1 = rationalNumber(1, 2)
    r2 = rationalNumber(1, 3)
    r3 = r1.__sub__(r2)
    assert r3.numerator == 1
    assert r3.denominator == 6


def test_rational_number_mul() -> None:
    r1 = rationalNumber(1, 2)
    r2 = rationalNumber(1, 3)
    r3 = r1.__mul__(r2)
    assert r3.numerator == 1
    assert r3.denominator == 6


def test_rational_number_div() -> None:
    r1 = rationalNumber(1, 2)
    r2 = rationalNumber(1, 3)
    r3 = r1.__truediv__(r2)
    assert r3.numerator == 3
    assert r3.denominator == 2


def test_rational_number_pow() -> None:
    r = rationalNumber(1, 2)
    r2 = r.__pow__(2)
    assert isinstance(r2, rationalNumber)
    assert r2.numerator == 1
    assert r2.denominator == 4


def test_rational_number_pow_negative() -> None:
    r = rationalNumber(1, 2)
    r2 = r.__pow__(-2)
    assert isinstance(r2, rationalNumber)
    assert r2.numerator == 4
    assert r2.denominator == 1


def test_rational_number_rpow() -> None:
    r = rationalNumber(1, 2)
    f = r.__rpow__(2)
    assert isinstance(f, float)
    assert f == 0.25
