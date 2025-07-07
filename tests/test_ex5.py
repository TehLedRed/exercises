from pytest import raises

from exercises.ex5 import binarySearch


def test_binarySearch_1() -> None:
    assert binarySearch(28, playlist=[8, 4, 16, 23, 32, 28])


def test_binarySearch_2() -> None:
    assert binarySearch(-1, playlist=[8, 4, 16, 23, 32, -1])


def test_binarySearch_3() -> None:
    with raises(ValueError, match="10 is not in the playlist."):
        binarySearch(10, playlist=[8, 4, 16, 23, 32, -1])
