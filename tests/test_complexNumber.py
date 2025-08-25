from exercises.complexNumber import complexNumber


def test_init() -> None:
    z = complexNumber(3, 4)
    assert z.a == 3 and z.b == 4


def test_conjugate() -> None:
    z = complexNumber(3, 4)
    conj = z.__conjugate__()
    assert conj.a == 3 and conj.b == -4


def test_abs() -> None:
    z = complexNumber(3, 4)
    assert z.__abs__() == 5


def test_absoluteSq() -> None:
    z = complexNumber(3, 4)
    assert z.__absoluteSq__() == 25


def test_add() -> None:
    z1 = complexNumber(3, 4)
    z2 = complexNumber(5, 6)
    result = z1.__add__(z2)
    assert result.a == 8 and result.b == 10


def test_sub() -> None:
    z1 = complexNumber(3, 4)
    z2 = complexNumber(5, 6)
    result = z1.__sub__(z2)
    assert result.a == -2 and result.b == -2


def test_mul() -> None:
    z1 = complexNumber(3, 4)
    z2 = complexNumber(5, 6)
    result = z1.__mul__(z2)
    assert result.a == -9 and result.b == 38


def test_reciprocal() -> None:
    z = complexNumber(3, 4)
    recip = z.__reciprocal__()
    assert abs(recip.a - 0.12) < 0.01 and abs(recip.b - (-0.16)) < 0.01


def test_div() -> None:
    z1 = complexNumber(3, 4)
    z2 = complexNumber(5, 6)
    result = z1.__div__(z2)
    assert abs(result.a - 0.6393) < 0.01 and abs(result.b - 0.0328) < 0.01


def test_exponentiation() -> None:
    z = complexNumber(1, 0)
    result = z.__exponentiation__()
    assert abs(result.a - 2.718) < 0.01 and abs(result.b) < 0.01
