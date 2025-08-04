from pytest import raises

from exercises.maxPrimeFactor import maxPrimeFactor


def test_maxPrimeFactor_input() -> None:
    for invalid in [-1, 0, 1]:
        with raises(ValueError, match="n must be greater than 1!"):
            maxPrimeFactor(invalid)


def test_maxPrimeFactor() -> None:
    assert maxPrimeFactor(13_195) == 29
    assert maxPrimeFactor(600_851_475_143) == 6_857
