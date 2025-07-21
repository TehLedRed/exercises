from pytest import raises

from exercises.armstrongNumber import isArmstrong


def test_isArmstrong() -> None:
    assert isArmstrong(407)


def test_isArmstrong_false() -> None:
    assert not isArmstrong(10)


def test_isArmstrongError() -> None:
    with raises(ValueError, match="Input cannot be negative"):
        isArmstrong(-1)


def test_isArmstrong_list_comprehension() -> None:
    assert all(isArmstrong(value) for value in [153, 370, 371, 407])


def test_isArmstrong_list_comprehension_filter() -> None:
    assert [371, 372, 408] == [
        value + 1 for value in [10, 370, 371, 407] if isArmstrong(value)
    ]
