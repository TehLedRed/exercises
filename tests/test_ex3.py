from pytest import raises

from exercises.ex3 import isArmstrong


def test_isArmstrong() -> None:
    assert isArmstrong(9)


def test_isArmstrongError() -> None:
    with raises(ValueError, match="Input list cannot be empty"):
        assert isArmstrong("")
