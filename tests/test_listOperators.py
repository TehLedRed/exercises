from exercises.listOperators import appendList, concatenateList, filterList, lengthList, foldLeftList, reverseList, foldRightList


def test_appendList() -> None:
    assert appendList([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert appendList([], [1, 2]) == [1, 2]
    assert appendList([1, 2], []) == [1, 2]
    assert appendList([], []) == []


def test_concatenateList() -> None:
    assert concatenateList([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert concatenateList([[], [], []]) == []
    assert concatenateList([[1], [2], [3]]) == [1, 2, 3]
    assert concatenateList([]) == []


def test_filterList() -> None:
    assert filterList(lambda x: x > 0, [1, -2, 3, -4, 5]) == [1, 3, 5]
    assert filterList(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]
    assert filterList(lambda x: x < 0, [-1, -2, -3]) == [-1, -2, -3]
    assert filterList(lambda x: x > 0, []) == []
    assert filterList(lambda x: x % 2 == 0, []) == []


def test_lengthList() -> None:
    assert lengthList([1, 2, 3, 4, 5]) == 5


def test_foldLeftList() -> None:
    assert foldLeftList(lambda acc, x: acc + x, [1, 2, 3, 4, 5], 0) == 15
    assert foldLeftList(lambda acc, x: acc * x, [1, 2, 3, 4, 5], 1) == 120
    assert foldLeftList(lambda acc, x: acc + x, [], 0) == 0
    assert foldLeftList(lambda acc, x: acc * x, [], 1) == 1


def test_reverseList() -> None:
    assert reverseList([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverseList([]) == []
    assert reverseList([1]) == [1]
    assert reverseList([1, 2]) == [2, 1]


def test_foldRightList() -> None:
    assert foldRightList(lambda x, acc: acc + x, [1, 2, 3, 4, 5], 0) == 15
    assert foldRightList(lambda x, acc: acc * x, [1, 2, 3, 4, 5], 1) == 120
    assert foldRightList(lambda x, acc: acc + x, [], 0) == 0
    assert foldRightList(lambda x, acc: acc * x, [], 1) == 1